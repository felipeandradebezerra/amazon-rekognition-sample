# Amazon Rekognition Code Sample - Part of a proof of life for pensioners

This repository contains an example code snippet showing how Amazon Rekognition can be used to avoid common fraud schemes in relation to submiting a proof of life through an app.

The full solution also uses the camera of the mobile phone to capture and detect faces with ML Kit on Android and iOS. It also prompts users to perform a challenge shared from the server side. For instance, users must move their eyes to a randomly defined target position. This triggers a series of verification processes that validate if:

- There was an image of one—and only one—face captured;
- A user kept his or her face at the center of the image and at the appropriate distance;
- A user moved his or her eyes to the target position;
- A user smile;
- A user performed a head rotation movement, mimicking a three-dimensional system.

### Dependencies

First, install the project dependencies:

```bash
$ pip install -r requirements.txt
```

