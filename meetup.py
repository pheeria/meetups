import requests
import json


def fetch(meetup, no_later_than):
  response = requests.get(f"https://api.meetup.com/{meetup}/events",
    params={ "no_later_than": no_later_than })
  return response.json()

def format(event):
  result = {}

  result["name"] = event["name"]
  result["link"] = event["link"]
  result["organizer"] = event["group"]["name"]
  result["location"] = event["venue"]["name"]
  result["address"] = event["venue"]["address_1"]
  result["address_link"] = f'https://www.google.com/maps/search/?api=1&query={event["venue"]["lat"]},{event["venue"]["lon"]}'
  result["description"] = event["description"]
  result["date"] = f'{event["local_date"]}, {event["local_time"]}'

  return result

def markdownify(event):
  result = f'''
## [{event["name"]}]({event["link"]})

**By:** {event["organizer"]}\n
**When:** {event["date"]}\n
**Where:** {event["location"]}, [{event["address"]}]({event["address_link"]})\n
**What:** {event["description"]}\n
---
'''
  return result

def main():
  with open("config.json", "r") as f:
    config = json.load(f)
  
  strings = [ f'# Upcoming meetups until {config["no_later_than"]}' ]

  for meetup in config["meetups"]:
    fetched = fetch(meetup, config["no_later_than"])
    for event in fetched:
      formatted = format(event)
      markdowned = markdownify(formatted)
      strings.append(markdowned)
  
  with open(f'{config["no_later_than"]}_meetups.md', "w") as f:
    f.writelines(strings)

if __name__ == "__main__":
  main()