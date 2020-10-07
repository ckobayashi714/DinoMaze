# Installation

__Computer Minimum Requirements:__

+ OS: Linux - Tuffix (Windows and MacOS will also work)
+ Window Resolution __1024 x 768__
+ CPU: Any
+ RAM: Any
+ GPU: Any
+ HDD: 20MB

__In order to run DINO MAZE on a machine, the user will need to complete the following steps:__

1. Check to make sure you have Python3 installed. Open a terminal window and type the following:

    ```shell
    which python3
    ```

    If you see a location success, you have Python3 installed.

2. Check to make sure you have the right version installed. In the same window type the following:

    ```shell
    python3 --version
    ```

    If you see version 3.7.5 or 3.7.7 success, you have the right version installed.

    ![Terminal to check for Python3](/screenshots/tuffix/1check_for_python3.png)

    If you don't have python3 installed or have the incorrect version you can install or update by following the steps on this link: [Install or Update Python3](https://www.itsupportwale.com/blog/how-to-upgrade-to-python-3-7-on-ubuntu-18-10/)

3. Once you have the correct Python3 version installed, we can now check for a __Virtual Environment__

4. Check to make sure you have Virtualenv installed. Open a terminal window and type the following:

    ```shell
    which virtualenv
    ```

    If you see a location success, you have virtualenv installed.

5. Check to make sure you have the right version installed. In the same window type the following:

    ```shell
    virtualenv --version
    ```

    If you see version 15.1.0 or above success, you have the right version.

    ![Terminal to check for Virtual Environment](/screenshots/tuffix/2check_for_virtualenv.png)

    If you don't have virtualenv installed or have an outdated version you can install or update by typing the following in a terminal window:

    ```shell
    pip install virtualenv (to install)
    pip install virtualenv --upgrade (to update)
    ```

6. Now we can create a virtual environment. To create a new virtual environment, navigate to the desktop. In a terminal window type the following:

    ```shell
    cd Desktop/
    ```

    You are now working on the Desktop

7. Let's create a new virtual environment for Python3. In the terminal window type:

    ```shell
    virtualenv --python=/usr/bin/python3 env && source env/bin/activate && pip install pygame==2.0.0dev6
    ```

    ![Terminal to create Virtual Environment](/screenshots/tuffix/3create_virtualenv.png)

    If you see this prompt, you have successfully created and activated a virtual environment for Python3 with Pygame version 2.0.0dev6.

8. Go to the top of the main repository page, navigate to the Clone section and click on "Download ZIP".

    ![Download Repo](/screenshots/tuffix/4download_repo.png)

9. After you've downloaded the file, open the zip folder and click on Extract.

    ![Extract Repo](/screenshots/tuffix/5open_repo_zip.png)

10. Extract the folder to the virtual environment folder you created earlier.

    ![Extract to folder](/screenshots/tuffix/6extract_repo.png)

11. Go back to the Desktop and open the env folder to see its contents. You should see the following:

    ![Env Folder](/screenshots/tuffix/7env_folder.png)

12. Open a new terminal and active the environment by typing the following:

    ```shell
    cd Desktop/
    source env/bin/activate
    ```

    ![Activate Environment](/screenshots/tuffix/8activate_vlen.png)

    If you see (env) on the left, success you have activated the environment.

13. In the same terminal window, navigate to the game folder by typing the following:

    ```shell
    cd env/
    cd cpsc-386-project-ckobayashi714-master/
    ```

    ![Go to Game](/screenshots/tuffix/9navigate_to_repo.png)

14. Now you can finally run the game. In the terminal window type the following:

    ```shell
    python3 game.py
    ```

    ![Run the Game](/screenshots/tuffix/10root_run_game.png)

    If you see the game title page DINO MAZE and hear music, you have successfully installed the game on your machine. Have fun!
