# Crafting-package-BD
A simple system for crafting For custom ballsdex instances.

**what changed(change log)**

new /craft begin command

new /craft add and remove command so it won't automatically delete 

better menu 

new /craft recipes command 

new crafting ingredient group 

> [!IMPORTANT]
> Any Bugs, errors, or confusion in steps You won't get any direct support from official Ballsdex server for this package since this is a custom one You need to directly contact @An Unknown Guy or just ping me on the Ballsdex Developer server server or direct message me 

> [!Tip]
> Read howtouse.txt to understand how to use this package 
> 
## Installation 

# Step 1 
Make a folder called `crafting` at your `BallsDex-DiscordBot/ballsdex/packages`
Copy the `__init__.py` `cog.py` file `models.py` file `crafting_utils.py` `logic.py` `crafting_views.py` and `session_manager.py` file to the new crafting folder you made 

# Step 2 
Add the package to your config.yml, open your config.yml scroll down until your see 
`packages` and add it there 
![IMG_20250506_154729](https://github.com/user-attachments/assets/c035eeaf-642d-4630-a5df-aaca6edb58ea)

# Step 3 
Open your `__main__.py` and edit the 
```py
TORTOISE_ORM = {
    "connections": {"default": os.environ.get("BALLSDEXBOT_DB_URL")},
    "apps": {
        "models": {
            "models": ["ballsdex.core.models"],
            "default_connection": "default",
        },
    },
}
```

To reflect the models in crafting folder ![IMG_20250506_155944](https://github.com/user-attachments/assets/412695ee-d6ca-4f29-bb28-9aa08167b978)

# Step 4 
create a folder named `craftings` in your `BallsDex-DiscordBot/admin_panel` and paste every file from the craftings
folder on this repository including the migration folder onto your craftings folder.
![IMG_20250506_161115](https://github.com/user-attachments/assets/3ce13bce-ffd5-4fc3-8754-cad022660036)

Adding screenshot to avoid any confusion

# Step 5 
Open your `BallsDex-DiscordBot/admin_panel/admin_panel/settings` open `local.py` and add this line 
```py
INSTALLED_APPS.append("craftings")
```
Then at your base admin_panel folder,
Run  

```py
docker compose exec admin-panel python3 manage.py makemigrations craftings
```
Then 

```py
docker compose exec admin-panel python3 manage.py migrate craftings
```
![Screenshot_2025-05-08-15-07-05-36](https://github.com/user-attachments/assets/b78825a4-8076-4c6f-873e-ced65451e7e2)


And Your Done 
> [!IMPORTANT]
> any issue regarding this part feel to dm me or ping me 
