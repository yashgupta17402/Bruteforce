# BRUTEFORCE - Wearable-Haptic-braille-device-for-Blind
![tv3](https://github.com/yashgupta17402/Wearable-Haptic-braille-device-for-Blind/assets/115718968/0cac9bf5-1b2e-4944-b03f-af12c4eb8a29)
</br>

# Table of Contents
1. [Existing Problem ](#existing-problem)
2. [Overview](#overview)
3. [Goals and Objective](#goals-and-objective)
4. [Block Diagram and Circuit Diagram](#block-diagram-and-circuit-diagram)
5. [Sensors and Hardware Components](#sensors-and-hardware-components)
6. [Code Description](#code-description)
7. [Video Link](#video-link)
8. 


## Touch Screen 
The Velostat sheet touch screen is interfaced with this code to read touch inputs. The 15x15 pressure matrix detects the touch points, allowing the device to trace finger movements.
The raw sensor values from the touch screen are read and .are  sent to the python for further processing .

![grid](https://github.com/yashgupta17402/Bruteforce/assets/115718968/fd72a646-66b9-4e22-ad50-5aef6ba83394)

</br>

## Touch Screen with haptic glove

![glove_withgrid](https://github.com/yashgupta17402/Bruteforce/assets/115718968/978cbd64-94aa-413c-b493-28e18252146f)

</br>

## Whiteboard for classroom experience

![whiteboard](https://github.com/user-attachments/assets/43983c42-4576-4f10-b3bb-7f51dde8cc01)

## Work Flow of Device
![pics](https://github.com/user-attachments/assets/f0122c93-8a74-4631-a179-2ae510487ad1)

## Components
![full_device](https://github.com/user-attachments/assets/182f213d-0705-41c2-ba40-01632cd1c555)




## Existing Problem 

Technological advances have enabled the development of various assistive solutions to aid
the visually impaired in their daily activities. One of the primary focus that continues to
persists is in developing an effective learning device that helps to not only read the
alphanumeric characters but also successfully read other spatial forms of learning such as
diagrams, signals and graphs especially in the science and engineering streams. Braille for
text in different formats including refreshable and portable devices are widely popular and
effective, but they are either not economical to the downtrodden family of students or limits
the use-case in the classroom setting. The real-time capability is not adhered, thereby the
visually impaired students are deprived of immersive learning in the classroom
environment. Although many refreshable braille devices are made available in the past
decade, however the context of the classroom board is still not mapped entirely to the
visually impaired students. The other constant challenge among the educators is expressing
spatially relevant information such as exponential and logarithmic expressions which are
either superscript or subscript in style to the impaired students.
## Overview
A novel wearable device that enables real-time haptic changes to reflect braille
representation of the classroom teaching including spatially relevant expressions and
diagrams around a learning workspace to provide a complete context aware classroom
board learning. The unique form of the device aids in easing the learning aspects in high
school and engineering levels thereby empowering the visually impaired students to take
up the science and engineering fields in the future.
## Goals and Objective
In STEM (Science, Technology, Engineering, and Mathematics) education, student typically
comes across exponential or logarithmic functions or even integral expressions at various
times. Hence for comprehensive learning, one cannot ignore perceiving spatially located
alpha-numeric characters for visually impaired students. Hence a device to assist or at least
alert the blinds to move around the position is very beneficial.
The wearable haptic design to addresses the challenges faced by blind individuals in
reading and comprehending spatially distant written information.
## Key Features
Real-time Haptic Feedback:

o The wearable device provides real-time haptic changes that convert
classroom teachings into braille representations.
o It effectively translates spatially relevant information, including diagrams,
signals, and graphs, which are crucial in STEM education.

Comprehensive Classroom Integration:

o The device is designed to map the entire classroom board context to
visually impaired students.
o It supports the learning of spatially located alphanumeric characters and
complex expressions such as exponential and logarithmic functions.

Affordability and Accessibility:

o The solution aims to be economical, making it accessible to students from
economically disadvantaged backgrounds.
o It is designed to be used both in classroom settings and personal learning
environments.
Empowerment in STEM Fields:

o By easing the learning process of high school and engineering concepts,
the device empowers visually impaired students to pursue careers in
science and engineering.
## Block Diagram and Ciruit Diagram
![tv](https://github.com/yashgupta17402/Wearable-Haptic-braille-device-for-Blind/assets/115718968/68c7fd33-e9ec-4bf6-a0e3-936e5ca22ac3)
![tv2](https://github.com/yashgupta17402/Wearable-Haptic-braille-device-for-Blind/assets/115718968/25a1bff5-26a6-4932-b36c-d7970cf73002)
</br>
## Velostat touch screen connections
![WhatsApp Image 2024-07-17 at 14 56 06](https://github.com/user-attachments/assets/4aed4e27-06fa-4880-bb40-6b33cb8de83c)
</br>

# Component Connections

## Velostat Sensor (X)
| Sensor Pin | Microcontroller Pin |
|------------|----------------------|
| VCC        | VCC                  |
| A0         | A0 THROUGH RESISTOR  |               |


## Velostat Sensor (Y)
| Sensor Pin | Microcontroller Pin |
|------------|----------------------|
| VCC        | VCC                  |
| A1         | A1 THROUGH RESISTOR  |  

## Coin Vibration Motor
| Motor Pin  | Microcontroller Pin |
|------------|----------------------|
| Common Ground | GND              |
| Motor-1    | D3                   |
| Motor-2    | D4                   |
| Motor-3    | D5                   |
| Motor-4    | D6                   |

## Mini Vibration Motor
| Motor Pin  | Microcontroller Pin |
|------------|----------------------|
| Common Ground | GND              |
| Motor-1    | D7                   |
| Motor-2    | D8                   |
| Motor-3    | D9                   |
| Motor-4    | D10                  |
| Motor-5    | D11                  |
| Motor-6    | D12                  |

Ensure all connections are secure and double-check each component's datasheet for any additional requirements or notes.
# Budget and Component Links

This section provides the estimated budget for the project along with links to purchase the components.

## Sensors and Hardware Components

| Component               | Quantity | Unit Price (INR) | Total Price (INR) | Purchase Link                                                                 |
|-------------------------|----------|------------------|-------------------|--------------------------------------------------------------------------------|
| Velostat                | 1        | 470              | 470              | [Buy Here](https://www.thingbits.in/products/pressure-sensitive-conductive-sheet-velostat-linqstat/)                            
| Coin Vibration Motor    | 6        | 48               | 288               | [Buy Here](https://sharvielectronics.com/product/coin-vibration-motor-flat-1034-mobile-phone-vibrator-motor-10mm/)                           
| Multiplexer             | 2        | 46               | 92               | [Buy Here](https://sharvielectronics.com/product/cd74hc4067-16-channel-analog-digital-multiplexer-breakout-board-module/)     
| Wires                   | 3        | 77               | 231              | [Buy Here](https://sharvielectronics.com/product/male-to-male-jumper-wire-connector-40-pieces/)) 
| 3D Prints               | 2        | 500              | 1000              | [Buy Here]                                     

## Boards

| Component               | Quantity | Unit Price (INR) | Total Price (INR) | Purchase Link                                                                 |
|-------------------------|----------|------------------|-------------------|--------------------------------------------------------------------------------|
| ESP32-c3                   | 1        | 536             | 536              | [Buy Here](https://sharvielectronics.com/product/seeed-studio-xiao-esp32c3-tiny-mcu-board-with-wifi-and-ble-battery-charge-supported-module/) 
| Arduino uno                | 1        | 475             | 475              | [Buy Here](https://sharvielectronics.com/product/uno-r3-development-board-compatible-with-arduino/)     |


## Total Estimated Budget

| Description             | Total Price (INR) |
|-------------------------|-------------------|
| Total Budget            | 3,092              |

# Video Link

https://youtu.be/BlAvIPSyD9E

# Code Description
### drawing.py 
Traces the hand movement on the touchscreen
### merge.py 
webserver which tracks the tracing of an identified figure of the professor
### output.py
Used to send commands to esp32 to make decisions about motor
### server.js ,board.html,whiteboard.js
Used for professor side's whiteboard .It saves the drawing drawn on whiteboard on server.
### shapes.py
Used for identifying shape of figure drawn.


# Future Work
Our future work will focus on several key areas to refine and expand the current project. These include:

## 1. Refinement of Design:
We aim to enhance the current design to incorporate six Braille pins within a wearable device. This integration will enable users to study both shapes and text through a single, convenient device. By making the device wearable, it will be more accessible and user-friendly, providing a seamless experience for users, especially those with visual impairments.

## 2. Development of a Smart Whiteboard:
We plan to develop a smart whiteboard that will enable teachers to draw shapes and write words, which will then be converted into Braille in real-time. This innovation will facilitate interactive learning environments, making it easier for visually impaired students to follow along with lessons and engage with the material being taught. The smart whiteboard will utilize advanced sensors and software to capture and translate written content accurately.

## 3. Enhancement of Machine Learning Models:
Future work will also focus on developing more sophisticated Machine Learning models to improve the accuracy and efficiency of converting written text into Braille formats. By leveraging advanced algorithms and larger datasets, we aim to create models that can better understand and translate a wider variety of handwriting styles and printed fonts into Braille. This will ensure that the system can handle diverse inputs and provide reliable Braille outputs for users.

## 5. Integration with Other Assistive Technologies:
To enhance the overall learning experience, we plan to integrate our device with other assistive technologies, such as screen readers and tactile graphics displays. This will create a more comprehensive educational toolkit for visually impaired users, allowing them to access a wider range of learning materials and resources.

## 6. Scalability and Cost-Effectiveness:
Finally, we will explore ways to make the device scalable and cost-effective, aiming to make it widely accessible to educational institutions and individuals. This will involve optimizing the production process and exploring funding opportunities to support the widespread adoption of the technology.








