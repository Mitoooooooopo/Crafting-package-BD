# Crafting-package-BD
A simple system for crafting For those who want a craft command for their Ballsdex instance 

## Installation 

# Step 1 
Make a folder called `crafting` at your `BallsDex-DiscordBot/ballsdex/packages`
Copy the `__init__.py` `cog.py` file `models.py` file and `transformer.py` file to the new crafting folder you made 

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
create a folder named `craftings` in your `BallsDex-DiscordBot/admin_panel` and paste every file from the craftings folder including including the migration folder into your craftings folder.
![IMG_20250506_161115](https://github.com/user-attachments/assets/3ce13bce-ffd5-4fc3-8754-cad022660036)

Adding screenshot to avoid any confusion

# Step 5 

