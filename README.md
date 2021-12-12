<h1>The Abandon Rate Generator</h1>

<p>Call center abandonment is a critical KPI, that must be closely monitored at all times. Abandon rate is the percentage of customers that abandon their call before speaking to a call center representative. This is calculated by dividing the number of abandonded calls by the total number of calls received. 
</p>

## Project Purpose
<p>This app is not intended to be used by multiple users at one time. This app was created for an individual call centre to track their perfomance by generating their abandon rate. It allows a user to generate the abandon rate as many times as they please. This app is available to any member of staff within the call center. Tracking this KPI will assist in adhering to SLA's, creating an overall better experience for the customer and improving the call centers performance. We also offer the user an option to view the spreadsheet for further data analysis.
</p>

## User Experience

### Target Audience Goals:
* An app that is easily navigated and interactive.
* An app that is clear and easy to digest.
* To understand the purpose of the app.
* An option to input data.
* To be provided with an abandon rate.
* An option to view all input data.

### App Owner Goals:
* An app that is clear and easy to navigate.
* Allow the user to input data.
* Create loyal users.
* Clearly explain the purpose of the app.
* Provide the user with the abandon rate.
* Give the user an option to view previous input data.

### User Stories
* As a app owner:
    * I want a simple and interactive user experience.
    * I want to clearly explain the purpose of the app and how an abandon rate is generated.
    * I want clear output data in the terminal.
    * I want the user to confirm their inputs before posting to the spreadsheet.
    * I want to provide the user with feedback if an incorrect input is entered.
    * I want to give the user the option to view all data inputs.

* As an app user:
    * I want to easily enter in data.
    * I want to be provided with feedback if the data entered is incorrect.
    * I want an option to confirm all my data is correct before submitting.
    * I want to be able to confirm my inputs before the abandon rate is generated.
    * I want a simple and easy to navigate app.
    * I want to understand the purpose of that app.

## Fuctional Scope
<p> The following flowchart displays the flow of "The Abandon Rate Generator".
</p>

![Flow Chart](https://raw.githubusercontent.com/AshFitz/abandon-rate-generator/main/assets/flowchart/flowchart.png)

## Features

### Welcome Message
<p>Welcomes the user to the app.</p>
*********************Insert Image

### Description
<p>Informs the user ont the meaning of abandon rate and explains the functionality.</p>
**************************Inset image

### User Options
<p>The user is provided with two options. One to generate an abandon rate and the other, to view prevous abandon rate inputs.</p>
*****************Insert Image

### Option 1: Generate an abandon rate
<p>The user will be requested to provide multiple inputs including their name, job title, departement, the number of inbound calls and the number of outbound calls. Before submitting the data the user must confirm if the inputs are correct. Once confirmed the user will be presented with the abandon rate %. If the details are incorrect the user has the option to return home to try again.</p>
*****************Insert all Images

### Option 2: View previous abandon rates
<p>The user will be provided with 3 options. To view the most recent abandon rate, a link to the spreadsheet to view all previous input data or to return home. If the user choses view the most recent abandon rate they will be provided with the last submission. They will provided with the URL of the spreadsheet if they chose the second option to view all of the inputs. The last option will return the user to the home page to start again if they chose. </p>
*****************Insert all Images

## Future Features
* I would like to provide the user with an input to provide the number of agents working during the times the inbound calls were recieved. When the data is analysed it may come to light they may have needed more staff which caused a hih abandon rate of calls. Over time the call center will have the data to forcast how busy it will be on certain days at certain times. The agent input will allow the call center to forcast how many agents they may need at those times to reduce the abandon rate. In turn this will help increase the overall performance of the call center.
* I would like to use a data base instead of a spreadsheet.

## Language Used
* Python 3.0

## Modules & API's Used
* OS
<p> This module allowed me to create and use a clear terminal function. This removed all previous input by the user and outputs by the generator. This helps the readability and flow.</p>

* Time
<p> This module allowed me to retrieve the current date, append it to the list and then post it to the spreadsheet. Using this allows the user to clearly see the date of the abandon rate entries when viewing previous abandon rates.
</p>

* Gspread
<p> Using gspread saves the users input and allows the user to view the data when requested.
</p>



