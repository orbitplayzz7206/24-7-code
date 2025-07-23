#!/usr/bin/env python3

import os
import random
import string
import time

def display_banner():
    print(r"""
       _     ___    __ ___       ___   ____  
      dM.    `MM    d'  `MMb     dMM'  6MMMMb/
     ,MMb     MM   d'   MMM.   ,PMM  8P    YM
     d'YM.    MM  d'    M`Mb   d'MM 6M      Y
    ,P `Mb    MM d'     M YM. ,P MM MM       
    d'  YM.   MMd'      M `Mb d' MM MM       
   ,P   `Mb   MMYM.     M  YM.P  MM MM       
   d'    YM.  MM YM.    M  `Mb'  MM MM       
  ,MMMMMMMMb  MM  YM.   M   YP   MM YM      6
  d'      YM. MM   YM.  M   `'   MM  8b    d9
_dM_     _dMM_MM_   YM._M_      _MM_  YMMMM9 
                                                       
                              
    """)

def generate_random_string(length=100):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def create_edit_delete_file():
    folder_name = "24"
    os.makedirs(folder_name, exist_ok=True)

    while True:
        try:
            file_name = os.path.join(folder_name, f"{generate_random_string(8)}.txt")

            with open(file_name, "w") as file:
                for _ in range(random.randint(10, 100)):
                    file.write(generate_random_string(100) + "\n")
            print(f"Created: {file_name}")

            time.sleep(2)

            with open(file_name, "w") as file:
                for _ in range(random.randint(10, 100)):
                    file.write(generate_random_string(100) + "\n")
            print(f"Edited: {file_name}")

            time.sleep(1)

            os.remove(file_name)
            print(f"Deleted: {file_name}")

            time.sleep(1)

        except Exception as e:
            print(f"An error occurred: {e}")
            time.sleep(5)

if __name__ == "__main__":
    display_banner()
    create_edit_delete_file()
