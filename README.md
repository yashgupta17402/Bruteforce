# BRUTEFORCE - Wearable-Haptic-braille-device-for-Blind
![tv3](https://github.com/yashgupta17402/Wearable-Haptic-braille-device-for-Blind/assets/115718968/0cac9bf5-1b2e-4944-b03f-af12c4eb8a29)
</br>

## Touch Screen 
The Velostat sheet touch screen is interfaced with this code to read touch inputs. The 15x15 pressure matrix detects the touch points, allowing the device to trace finger movements.
The raw sensor values from the touch screen are read and .are  sent to the python for further processing .

![grid](https://github.com/yashgupta17402/Bruteforce/assets/115718968/fd72a646-66b9-4e22-ad50-5aef6ba83394)

</br>
## Touch Screen with haptic glove

![glove_withgrid](https://github.com/yashgupta17402/Bruteforce/assets/115718968/978cbd64-94aa-413c-b493-28e18252146f)


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

# Component Connections

## Distance Sensor (X)
| Sensor Pin | Microcontroller Pin |
|------------|----------------------|
| VCC        | VCC                  |
| GND        | GND                  |
| SDA        | SDA                  |
| SCL        | SCL                  |
| Signal     | D1                   |

## Distance Sensor (Y)
| Sensor Pin | Microcontroller Pin |
|------------|----------------------|
| VCC        | VCC                  |
| GND        | GND                  |
| SDA        | SDA                  |
| SCL        | SCL                  |
| Signal     | D2                   |

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

# Future Work
The future work will include refining the design and including the six braille pins in a wearable form to make a single device for studying shapes and text in a single device. We plan to make a smart whiteboard for teacher to draw the shapes and write words. Also future work will include coming up with better Machine Learning Models to
convert written text to braile formats.






