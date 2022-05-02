# BurmaShaveBot

This one will need a little background information. In the early- to mid- 20th century, Burma-Shave famously ran a line of popular advertisements on roadside signs. The ads took the form of humorous five- to six-line poems, with one line displayed per sign. Poems would be revealed as drivers progressed down the highway. The following is an example of one of the original ads from 1929:

    Every shaver
    Now can snore
    Six more minutes
    Than before
    By using
    Burma-Shave


Over time, the ads began to cover other topics, including current events:

    Let's make Hitler
    And Hirohito
    Look as sick as
    Old Benito
    Buy defense bonds
    Burma-Shave

and driving safety:

    Drive
    With care
    Be alive
    When you
    Arrive
    Burma-Shave

I have several relatives who grew up in the era when these ads were being run, and took a liking to them. In family messaging threads, they will often convey ideas by writing silly poems in the Burma-Shave format. With this project, I thought I would write a simple bot that could write its own poems in the style of the Burma-Shave ads, and send them out to family members. 

In order to achieve this, I compiled a CSV file containing all the original poems (sourced from http://www.skypoint.com/members/schutz19/burma2.htm) and used that data to fine-tune GPT-2. `Generate-helper.py` generates a new set of ads using the resulting model, screens them by certain basic rules, and then returns a single poem to be sent as a text message. `Send-helper.py` contains functions which will send messages either by email-to-SMS gateway, or by the Twilio API service. 

Sending by Twilio allows you to send messages to a group chat, but requires you to verify phone numbers for all recipients on the free tier. Sending by email-to-SMS gateway does not require any personal data or number verification, but does not allow you to send group messages.

Required information for message delivery, including phone numbers and email addresses, must be defined in the config files.