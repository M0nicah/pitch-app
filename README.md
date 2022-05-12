# pitch-app
Pitchly is a pitch web application.
This application enables user/(s) to create accounts so that they can post their impressions. Users must login in order to view other pitch categories.

## Installation

Guide to install Pitchly application:

### Clone this repository
```bash
git clone https://github.com/M0nicah/pitch-app.git
```
* Move into the cloned directory:
```bash
cd pitch-app
```
* Create and activate your virtual environment:
```bash
mkvirtualenv virtual
```
* Install project dependancies within your active environment: (Read: requirements.txt and use command below)
```bash
(virtual)$ pip install -r requirements.txt
```
* Environment variables:
    *  Create a file called ```.env``` in the root folder
    ```bash
    (virtual)$ touch .env
    ```
    * Add the following lines to the file as seen in ```.env-template```
    ```bash 
    SECRET_KEY=
    DATABASE_URL=
    ```
* Start the flask server
```bash
(Virtual)$ flask run
```
* or

```bash
(Virtual)$ python3 manage.py
```
## Features and BDD

- Users are able to create user profile and login to post their pitch.

## Technology Used

- **Framework:** Flask
- **Language** Python

### Developed with
- **Structure:** Bootstrap, HTML

- **Styles:** CSS

## Author

* Designed and developed by: [Monica Masae](https://github.com/M0nicah)
