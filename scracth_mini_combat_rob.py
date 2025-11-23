Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

import random
import time

... # --- Basic Light Effect Function ---
... def light_effect(color):
...     print(f"[LİGHT] {color} glow activated...")
...     time.sleep(0.3)
... 
... # Attack function
... def attack():
...     damage = random.randint(5,20)
...     light_effect("RED")
...     print(f"[BOT] Attack executed! Target damage: {damage}")
...     return damage
... 
... # --- Move function ---
... def move(direction):
...     if direction not in ["forward", "back", "left", "right"]:
...         print("[Error] İnvalid direction!")
...         return
... 
...     light_effect("BLUE")
...     print(f"[BOT] Moving {direction}...")
... 
... # --- Main combat loop ---
... def main():
...     print("=== MINI COMBAT BOT ONLINE ===")
...     health = 100
... 
...     while health > 0:
...         print("\nChoose an action:")
...         print("1 - Move")
...         print("2 - Attack")
...         print("3 - Shutdown")
... 
...         choice = input("Action: ")
... 
...         if choice == "1":
...             direction = input("Direction (forward/back/left/right): ").lower()
...             move(direction)
... 
...         elif choice == "2":
...             dmg = attack()
            print(f"[SYSTEM] Damage log: {dmg}")
        elif choice == "3":
            print("[SYSTEM] shutting down...")
        else:
            print("[WARNING] Unknown command!")

        if random.random() < 0.2:
            hit = random.randint(1,10)
            health -= hit
            print(f"[ALERT] Enemy hit! -{hit} HP")
            light_effect("Yellow")

    print("\n[BOT] System offline.")

# --- Run progrsm ---
if __name__ == "__main__":
    main()


