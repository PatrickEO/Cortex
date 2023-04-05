import pytchat
import time

ID = input('ID: ')

chat = pytchat.create(video_id=ID)
while chat.is_alive():
    for c in chat.get().sync_items():
           print(f"{c.datetime} [{c.author.name}]- {c.message}")
           