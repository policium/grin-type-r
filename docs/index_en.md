# GRIN Type-R Assembly Instructions

## Introduction

Thank you for your purchase of GRIN Type-R. This kit requires soldering and firmware writing operations. Please follow the steps below to assemble.

## Precautions

This product is compatible with Cherry MX switches and compatible products. The keycaps are assumed to be 19mm pitch 18mm square, but we cannot guarantee compatibility.  

## Heading

1．Preparation  
2. Checking the kit contents  
3. Initial operation check  
4. Soldering diodes  
Soldering the PCB socket for the switch  
6. Install the stabilizer  
7. Screw the switch plate to the PCB  
8. Install the switch  
9. Attach the top plate and PCB  
10. Attach the feet to the bottom plate  
11. Attach the bottom plate.  
Attach the key cap.  
13. Operation check  
14. 3D printed case  
A1. Appendix  

## 1. Preliminary preparation

## Determine the array
For GRIN Type-R, you can choose a combination of ANSI, ISO, JIS layout, single space bar and split space bar. Since the number of switches and keycaps required for each of them varies, it is necessary to decide in advance.

! [layout](https://user-images.githubusercontent.com/3132296/146913502-217302a7-877f-430a-b0cc-7842f74d1557.png)

### Prepare the parts you will need in addition to the kit.
- Keycaps (Cherry MX compatible) ... to match the selected layout.  
[YUSHA KOUBOU](https://shop.yushakobo.jp/collections/keycaps)  
[TALP KEYBOARD](https://talpkeyboard.net/?category_id=59be183f428f2d49120007b1)  
- Keyswitch (Cherry MX compatible) ... * Matches the selected keyboard layout.  
[Yusha Kobo](https://shop.yushakobo.jp/collections/all-switches)  
[TALP KEYBOARD](https://talpkeyboard.net/?category_id=59cf8860ed05e668db003f5d)  
- PCB socket for Cherry MX switches ... * Matches the selected layout.  
Not required if you want to install the key switch directly.  
[Yusha Kobo](https://shop.yushakobo.jp/products/a01ps)  
[TALP KEYBOARD](https://talpkeyboard.net/items/5e02c5405b120c792616bcf9)  
- Stabilizer (PCB mount) ... *Adjust to the selected layout.  
[Yusha Kobo](https://shop.yushakobo.jp/products/a0500st?variant=37665699430561)  
[TALP KEYBOARD](https://talpkeyboard.net/?category_id=5f884b9b3313d216eb50558a)  
- Wire for 3U stabilizer ... * Matches the selected array  
This is required if you want to use a space bar that is not split. The wire size is not common, so please make your own or purchase separately from Yusha Kobo.  
[Yusha Kobo](https://shop.yushakobo.jp/products/a0500st?variant=40429698678945)
- USB Type-C cable (for data communication) ... 1  
- Micro USB cable (for data communication) ... 1pc  
To check Pico's operation

### Prepare the tools
- Soldering iron (for electronic circuit boards)
- Solder
- Flux
- Flux cleaner (IPA or other alcohol or solvent can be substituted)
- Tweezers
- Nippers
- Phillips screwdriver (No.0)
- Tissues

### Other things you might want to have
- Silicone work mat
- Rags, Kim wipes, cotton swabs
- Masking tape
- Desoldering wire, desoldering machine
- Tester (for investigating the cause of problems)

## 2. Check the contents of the kit
Please make sure you have the following items.
If any of these items are missing, please send us a message using the email icon at the top of the Booth store website.
- Bag➀  
    - Board (PCB) ... 1 piece  
    - Top Plate (FR-4) ... 1 piece  
    - Switch Plate (Aluminum or FR-4) ... 1 piece  
    - Bottom Plate (FR-4) ... 1 piece  
- Bag➁  
    - Diode (1N4148) ... 75 pcs
- Bag➂  
    - M2 screw (silver) ... 6 pcs
    - Short spacers (round, both female threads) ... 3  
- Bag➃  
    - M2 screw (black) ... 16 pcs.  
    - Long spacer (round female screw) ... 8 pcs  
    - Spacer thick (round, hollow) ... 8 pcs  
- Bag➄  
    - Plastic washer ... 8 pcs  
    - Rubber washer ... 24 pcs  
- Bag ➅  
    - Aluminum feet ... 2 pcs
    - M4 screw ... 2 pcs
    - Rubber feet ... 2 pcs

## 3. Initial Operation Check

Remove the board from the bag➀.
The shipped board has the ANSI version of PRK Firmware already written on it. This is the first step in confirming that it works properly.  

### Connect the board to the PC and make sure it is recognized.

Connect the board to the PC with a USB cable. Connect the board to the PC with a USB cable and make sure the drive "PRKFirmware" is recognized.  

### Connect the board to the PC with a USB cable.

[IMG_20211024 [IMG_20211024_184022__01](https://user-images.githubusercontent.com/3132296/138600349-d7a1206c-a3c7-4663-90a5-6ad1bfbf6f9c.jpg)  
Short-circuit the two points in the picture with tweezers or other conductors, and check that "1" is input. If it does not, please send us a message from the mail icon at the top of the Booth store website.

The key layout is set to ANSI in the shipping state.  

## 4. Soldering the diode

Attach the diodes from the bag➁ to the board.  

Attention!  
Depending on the key layout and the way the switch is installed, there may be positions where the diode does not need to be installed.  
Do not install the diodes in unnecessary positions as they may interfere with the stabilizer.  
Refer to the layout image in red for the required diodes.

Caution!  
Some diodes are oriented differently from others. Please look at the silk carefully and mount them correctly.  

Bend the legs of the diode.  
Bend the legs of the diode. [IMG_20211024_185426__01](https://user-images.githubusercontent.com/3132296/138599397-515d71bd-303b-48e0-98fb-fd6c56f75fc6.jpg)

Align the direction of the silk with the direction of the diode and set it.  
! [IMG_20211024_185451__01](https://user-images.githubusercontent.com/3132296/138599443-0b524bb9-5166-402d-975e-d0db50a08e34.jpg)

Fix the diode with masking tape.  
! [IMG_20211024_185700__01](https://user-images.githubusercontent.com/3132296/138599491-e0bae086-d260-48b1-b428-10e3a5f24a5f.jpg)

Turn it over and solder it.  
! [IMG_20211024_185829__01](https://user-images.githubusercontent.com/3132296/138599533-31aaaf06-3e98-4a53-ac3d-a49286c5c794.jpg)

Cut off the legs with nippers and clean up the surrounding area with a flux cleaner.  
! [IMG_20211024_190343__01](https://user-images.githubusercontent.com/3132296/138599571-aa82a8cc-f0f4-4994-95de-8e2329e0151e.jpg)

## 5. Solder the PCB socket for the switch

If you want to mount the switch directly, skip this step.

Place the socket and solder it. Solder the socket while holding it with tweezers to prevent it from floating.  
[IMG_20211024 [IMG_20211024_191023__01](https://user-images.githubusercontent.com/3132296/138601716-b302675a-c47f-4df0-85e3-4094c506b9ff.jpg)

The orientation shown in the picture below is wrong.  
! [IMG_20211024_190934__01](https://user-images.githubusercontent.com/3132296/138602574-db98be8a-e68b-4710-9918-185e2c19d15a.jpg)

## 6. Installing the stabilizer

Install the 2U stabilizer for backspace, shift key, enter key and ISO enter of 2U or larger size.  
! [img_20211024_201044__01](https://user-images.githubusercontent.com/3132296/138602682-9a904d91-1ccc-49bf-b053-58f890d8d942.jpg)

Install the 3U wire stabilizer for the 3U space bar.  

## 7. Screw in the switch plate and the board.

Screw the switch plate to the board in three places with the bag➂ screws and spacers.  
! [img_20211025_012308](https://user-images.githubusercontent.com/3132296/138603250-d2de6202-2906-4cfb-a936-b46ea861370a.jpg)

! [img_20211024_202016__01](https://user-images.githubusercontent.com/3132296/138603264-aa535f03-cefc-45b1-8bed-a865e45260f8.jpg)

## 8. Install the switch.

For sockets, stick the switch in, being careful not to bend the switch terminals.  
For direct mounting, solder the switch from the back. When soldering, be careful not to let the switch float.  
[IMG_20211024 [IMG_20211024_204917__01](https://user-images.githubusercontent.com/3132)

Translated with www.DeepL.com/Translator (free version)
