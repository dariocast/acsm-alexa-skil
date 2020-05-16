# Multi Stream Audio Player Sample Skill (using ASK Python SDK)

The Alexa Skills Kit now allows developers to build skills that play long-form audio content on Alexa devices.  This sample project demonstrates how to use the new interfaces for triggering playback of audio and handling audio player input events.

## How to Run this skill

You will need to comply to the prerequisites below and to change a few configuration files before creating the skill and upload the lambda code.

### Pre-requisites

0. This skill uses the [ASK Python SDK](https://alexa-skills-kit-python-sdk.readthedocs.io/en/latest/) packages for developing the Alexa skill. 

    ```
    $ pip install virtualenv
    $ virtualenv skill_env
    $ skill_env\Scripts\activate
    $ pip install -r lambda/py/requirements.txt
    ```

1. You need an [AWS account](https://aws.amazon.com) and an [Amazon developer account](https://developer.amazon.com) to create an Alexa Skill.

### Deployment

Copy all file under ``./lambda/py/`` to ``./skill_env/Lib/site-packages``, then zip all file into 
``site-packages`` to ``skill.zip`` and upload it to the Lambda funtion

On Alexa Developer Console turn on ``AudioPlayer`` in Custom -> Interfaces and set through JSON Editor the JSON model ``it-IT.json``


## On Device Tests

To invoke the skill from your device, you need to login to the Alexa Developer Console, and enable the "Test" switch on your skill.

See https://developer.amazon.com/docs/smapi/quick-start-alexa-skills-kit-command-line-interface.html#step-4-test-your-skill for more testing instructions.

Then, just say :

```text
Alexa, avvia san michele.
```

## How it Works

Alexa Skills Kit now includes a set of output directives and input events that allow you to control the playback of audio files or streams.  There are a few important concepts to get familiar with:

* **AudioPlayer directives** are used by your skill to start and stop audio playback from content hosted at a publicly accessible secure URL.  You  send AudioPlayer directives in response to the intents you've configured for your skill, or new events you'll receive when a user controls their device with a dedicated controller (see PlaybackController events below).
* **PlaybackController events** are sent to your skill when a user selects play/next/prev/pause on dedicated hardware controls on the Alexa device, such as on the Amazon Tap or the Voice Remote for Amazon Echo and Echo Dot.  Your skill receives these events if your skill is currently controlling audio on the device (i.e., you were the last to send an AudioPlayer directive).
* **AudioPlayer events** are sent to your skill at key changes in the status of audio playback, such as when audio has begun playing, been stopped or has finished.  You can use them to track what's currently playing or queue up more content.  Unlike intents, when you receive an AudioPlayer event, you may only respond with appropriate AudioPlayer directives to control playback.

You can learn more about the new [AudioPlayer interface](https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/custom-audioplayer-interface-reference) and [PlaybackController interface](https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/custom-playbackcontroller-interface-reference).

## Cleanup

If you were deploying this skill just for learning purposes or for testing, do not forget to clean your AWS account to avoid recurring charges for your DynamoDB table.

- delete the lambda function 
- delete the IAM execution role 
- delete the DynamoDB table (Audio-Player-Multi-Stream)
