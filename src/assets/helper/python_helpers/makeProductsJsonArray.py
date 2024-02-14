# Python code to transform the given array into the desired format for all products
import random
# Original data arrays
projectors_benq = [
    # ... (existing BenQ projectors, first 6 already transformed)
    {
    "id": "7",
    "name": "BenQ MS560P Projector",
    "price": "₹ 32,500",
    "img": {
      "src": "https://5.imimg.com/data5/SELLER/Default/2023/11/361169334/QG/KC/RO/3098002/benq-ms560p-projector-500x500.jpg",
      "alt": "BenQ MS560P Projector"
    }
  },
  {
    "id": "8",
    "name": "BenQ MS550 Meeting Room Projector",
    "price": "₹ 31,500",
    "img": {
      "src": "https://5.imimg.com/data5/SELLER/Default/2023/11/361149907/AF/CS/PO/3098002/benq-ms550-projector-500x500.jpg",
      "alt": "BenQ MS550 Meeting Room Projector"
    }
  },
  {
    "id": "9",
    "name": "BenQ MX808PST+ Projector",
    "price": "₹ 50,000",
    "img": {
      "src": "https://5.imimg.com/data5/SELLER/Default/2023/11/361166848/JU/WX/KL/3098002/benq-mx808pst-projector-500x500.jpg",
      "alt": "BenQ MX808PST+ Projector"
    }
  },
  {
    "id": "10",
    "name": "BenQ MX808STH Interactive Projector",
    "price": "₹ 51,500",
    "img": {
      "src": "https://5.imimg.com/data5/SELLER/Default/2023/11/361000660/QR/HV/IQ/3098002/xerox-photocopiers-500x500.jpg",
      "alt": "BenQ MX808STH Interactive Projector"
    }
  },
  {
    "id": "11",
    "name": "BenQ GS50 Potrable Projector",
    "price": "₹ 69,990",
    "img": {
      "src": "https://5.imimg.com/data5/SELLER/Default/2023/11/360999536/TT/DJ/HI/3098002/office-automation-service-500x500.jpg",
      "alt": "BenQ GS50 Potrable Projector"
    }
  },
  {
    "id": "12",
    "name": "BenQ Th690st Projector",
    "price": "₹ 1,09,990",
    "img": {
      "src": "https://5.imimg.com/data5/SELLER/Default/2023/11/361155103/FE/ZJ/LU/3098002/benq-th690st-projector-500x500.jpg",
      "alt": "BenQ Th690st Projector"
    }
  },
  {
    "id": "13",
    "name": "BenQ LW500ST Projector",
    "price": "₹ 54,990",
    "img": {
      "src": "https://5.imimg.com/data5/SELLER/Default/2023/11/361155734/GD/MG/BT/3098002/benq-lw500st-projector-500x500.png",
      "alt": "BenQ LW500ST Projector"
    }
  },
  {
    "id": "14",
    "name": "BenQ MX550 Projector",
    "price": "₹ 37,300",
    "img": {
      "src": "https://5.imimg.com/data5/SELLER/Default/2023/11/361155968/BX/ZQ/JQ/3098002/benq-mx550-projector-500x500.jpg",
      "alt": "BenQ MX550 Projector"
    }
  }
    # ... (add the remaining BenQ projectors)
]

projectors_viewsonic = [
    # ... (ViewSonic projectors data)
    {
    "id": "1",
    "name": "ViewSonic LS751HD Projector",
    "price": "₹ 2,80,000",
    "img": {
      "src": "https://5.imimg.com/data5/SELLER/Default/2023/11/360399256/RV/OF/VK/3098002/viewsonic-ls751hd-projector-500x500.jpg",
      "alt": "ViewSonic LS751HD Projector"
    }
  },
  {
    "id": "2",
    "name": "ViewSonic LS550WHE Projector",
    "price": "₹ 61,500",
    "img": {
      "src": "https://5.imimg.com/data5/SELLER/Default/2023/11/361135043/PQ/TQ/XD/3098002/viewsonic-ls550whe-projector-500x500.jpg",
      "alt": "ViewSonic LS550WHE Projector"
    }
  },
  {
    "id": "3",
    "name": "ViewSonic CPB701HD Projector",
    "price": "₹ 62,299",
    "img": {
      "src": "https://5.imimg.com/data5/SELLER/Default/2023/11/361134787/UB/QO/DR/3098002/viewsonic-cpb701hdh-projector-500x500.jpg",
      "alt": "ViewSonic CPB701HD Projector"
    }
  },
  {
    "id": "4",
    "name": "ViewSonic CPB701-4K Home Projector",
    "price": "₹ 1,18,900",
    "img": {
      "src": "https://5.imimg.com/data5/SELLER/Default/2023/11/360398543/CB/JA/KP/3098002/viewsonic-cpb701-4k-home-projector-500x500.jpg",
      "alt": "ViewSonic CPB701-4K Home Projector"
    }
  },
  {
    "id": "5",
    "name": "ViewSonic M1+_G2 Smart  Portable Projector",
    "price": "₹ 46,000",
    "img": {
      "src": "https://5.imimg.com/data5/SELLER/Default/2023/11/360397098/JB/GH/QN/3098002/viewsonic-m1-g2-854x480-resolution-led-projecto-500x500.jpg",
      "alt": "ViewSonic M1+_G2 Smart  Portable Projector"
    }
  },
  {
    "id": "6",
    "name": "ViewSonic PA503X Projector",
    "price": "₹ 39,700",
    "img": {
      "src": "https://5.imimg.com/data5/SELLER/Default/2023/11/360396412/PQ/GD/FC/3098002/viewsonic-pa503x-projector-500x500.jpg",
      "alt": "ViewSonic PA503X Projector"
    }
  },
  {
    "id": "7",
    "name": "ViewSonic PA503S-3 Projector",
    "price": "₹ 29,990",
    "img": {
      "src": "https://5.imimg.com/data5/SELLER/Default/2023/11/360395316/OG/GV/CK/3098002/viewsonic-pa503s-3-projector-500x500.jpg",
      "alt": "ViewSonic PA503S-3 Projector"
    }
  }
]

projectors_egate = [
    # ... (EGATE projectors data)
    {
    "id": "1",
    "name": "EGATE I9 Pro Max Android Projector",
    "price": "₹ 12,990",
    "img": {
      "src": "https://5.imimg.com/data5/SELLER/Default/2023/11/361134778/LR/AA/SS/3098002/egate-i9-pro-max-android-projector-500x500.jpg",
      "alt": "EGATE I9 Pro Max Android Projector"
    }
  },
  {
    "id": "2",
    "name": "EGATE K9 Pro Max Android Projector",
    "price": "₹ 15,500",
    "img": {
      "src": "https://5.imimg.com/data5/SELLER/Default/2023/11/361073635/EB/RF/QY/3098002/egate-k9-pro-max-android-projector-500x500.jpg",
      "alt": "EGATE K9 Pro Max Android Projector"
    }
  },
  {
    "id": "3",
    "name": "EGATE L9 Pro Android Projector",
    "price": "₹ 21,990",
    "img": {
      "src": "https://5.imimg.com/data5/SELLER/Default/2023/11/361134831/VI/KS/AW/3098002/egate-l9-pro-android-projector-500x500.jpg",
      "alt": "EGATE L9 Pro Android Projector"
    }
  },
  {
    "id": "4",
    "name": "EGATE O9 Pro Zen Projector",
    "price": "₹ 25,990",
    "img": {
      "src": "https://5.imimg.com/data5/SELLER/Default/2023/11/360985723/WE/SX/AM/3098002/epson-digital-projector-500x500.jpg",
      "alt": "EGATE O9 Pro Zen Projector"
    }
  },
  {
    "id": "5",
    "name": "EGATE O9 Pro Automatic Smart Projector",
    "price": "₹ 25,990",
    "img": {
      "src": "https://5.imimg.com/data5/SELLER/Default/2023/11/361134818/AQ/KW/TS/3098002/egate-o9-pro-automatic-smart-projector-500x500.jpg",
      "alt": "EGATE O9 Pro Automatic Smart Projector"
    }
  }
]

projectors_epson = [
    # ... (EPSON projectors data)
    {
    "id": "1",
    "name": "Epson EB-E01 XGA 3LCD Projector",
    "price": "₹ 33,333",
    "img": {
      "src": "https://5.imimg.com/data5/SELLER/Default/2023/11/360394543/UM/LI/SZ/3098002/epson-eb-e01-xga-3lcd-projector-500x500.jpg",
      "alt": "Epson EB-E01 XGA 3LCD Projector"
    }
  },
  {
    "id": "2",
    "name": "Epson CO-FH02 Lumen Projector",
    "price": "₹ 80,000",
    "img": {
      "src": "https://5.imimg.com/data5/SELLER/Default/2023/11/361134899/HL/LB/BU/3098002/epson-co-fh02-lumen-projector-500x500.jpg",
      "alt": "Epson CO-FH02 Lumen Projector"
    }
  }
]

# Combine all projectors into a single array
all_projectors = projectors_benq + projectors_viewsonic + projectors_egate + projectors_epson
all_projectors = [
    {
        "id": 1,
        "img": "https://raw.githubusercontent.com/xXWarMachineRoXx/MairEnterprises/main/src/assets/images/benq.png",
        "alt": "BenQ EH600 Smart Projector",
        "category": "Top Rated",
        "brand": "BenQ",
        "type":"projector",
        "numberofReviews": 15,
        "canWishlist": "false",
        "averageRating": 4.5,
        "productName": "BenQ EH600 Smart Projector",
        "productLink": "BenQ-EH600-Smart-Projector",
        "price": "74,900",
        "description": "Advanced smart projector with high-resolution display.",
        "techspecs": {
            "displaytype": "DLP",
            "resolution": "Full HD (1920 x 1080)",
            "brightness": "3500 Lumens",
            "contrast": "20,000:1",
            "series": "Conference Room Projectors",
            "weight": "2.9 kg",
            "lightsource": "Lamp",
            "displaycolor": "1.07 Billion Colors",
            "aspectratio": "16:9",
            "throwratio": "1.5 - 1.65 (100\" @ 3.32 m)",
            "zoomratio": "1.1:1",
            "model": "EH600",
            "lamp": "Up to 15,000 hours",
            "warranty": "3 years"
        },
        "fulldescription":{
            "firstline":"Convenience made easier through wireless connections, built-in business apps, and over-the-air firmware updates.",
            "secondline":"Wireless projection & mirroring capabilities across various platforms (Mac/iOS, Android, or PC) for simple and easy presentations.",
            "thirdline":"Wireless projector with internet connectivity and USB reading to easily show your ideas during huddle sessions."
        }
        
    },
    {
        "id": 2,
        "img": "https://technosales.co.in/wp-content/uploads/2022/07/th685p.jpg",
        "alt": "BenQ TH685P Projector",
        "category": "Top Rated",
        "brand": "BenQ",
        "type":"projector",
        "numberofReviews": 25,
        "canWishlist": "false",
        "averageRating": 4.5,
        "productName": "BenQ TH685P Projector",
        "productLink": "BenQ-TH685P-Projector",
        "price": "79,000",
        "description": "High-performance projector for gaming and home theater.",
        "fulldescription":{
            "firstline":"Convenience made easier through wireless connections, built-in business apps, and over-the-air firmware updates."
            ,"secondline":"Wireless projection & mirroring capabilities across various platforms (Mac/iOS, Android, or PC) for simple and easy presentations."
            ,"thirdline":"Wireless projector with internet connectivity and USB reading to easily show your ideas during huddle sessions."
        },
        "techspecs": {
            "displaytype": "DLP",
            "resolution": "Full HD (1920 x 1080)",
            "brightness": "3500 Lumens",
            "contrast": "10,000:1",
            "series": "Home Entertainment Projectors",
            "weight": "2.9 kg",
            "lightsource": "Lamp",
            "displaycolor": "1.07 Billion Colors",
            "aspectratio": "16:9",
            "throwratio": "1.50 - 1.65 (100\" @ 3.32 m)",
            "zoomratio": "1.1:1",
            "model": "TH685P",
            "lamp": "Up to 15,000 hours",
            "warranty": "3 years"
        }
        

    },
    {
        "id": 3,
        "img": "https://5.imimg.com/data5/SELLER/Default/2023/11/361146632/PR/LF/AC/3098002/benq-mh560-projector-500x500.jpg",
        "alt": "BenQ MH560 Room Projector",
        "category": "Top Rated",
        "brand": "BenQ",
        "type":"projector",
        "numberofReviews": 30,
        "canWishlist": "false",
        "averageRating": 4.5,
        "productName": "BenQ MH560 Room Projector",
        "productLink": "BenQ-MH560-Room-Projector",
        "price": "59,990",
        "description": "Versatile room projector for both professional and personal use.",
        "fulldescription":{
            "firstline":"Convenience made easier through wireless connections, built-in business apps, and over-the-air firmware updates."
            ,"secondline":"Wireless projection & mirroring capabilities across various platforms (Mac/iOS, Android, or PC) for simple and easy presentations."
            ,"thirdline":"Wireless projector with internet connectivity and USB reading to easily show your ideas during huddle sessions."
        },
        "techspecs": {
            "displaytype": "DLP",
            "resolution": "Full HD (1920 x 1080)",
            "brightness": "3500 Lumens",
            "contrast": "10,000:1",
            "series": "Home Entertainment Projectors",
            "weight": "2.9 kg",
            "lightsource": "Lamp",
            "displaycolor": "1.07 Billion Colors",
            "aspectratio": "16:9",
            "throwratio": "1.50 - 1.65 (100\" @ 3.32 m)",
            "zoomratio": "1.1:1",
            "model": "TH685P",
            "lamp": "Up to 15,000 hours",
            "warranty": "3 years"
        }
    },
    {
        "id": 4,
        "img": "https://5.imimg.com/data5/SELLER/Default/2023/11/361171059/UY/GL/RF/3098002/benq-tk700-projectors-500x500.jpg",
        "alt": "BenQ TK700 Projector",
        "category": "Top Rated",
        "brand": "BenQ",
        "type":"projector",
        "numberofReviews": 172,
        "canWishlist": "false",
        "averageRating": 4.2,
        "productName": "BenQ TK700 Projectors",
        "productLink": "BenQ-TK700-Projector",
        "price": "1,49,990",
        "description": "State-of-the-art projector for an immersive gaming experience."
    },
    {
        "id": 5,
        "img": "https://5.imimg.com/data5/SELLER/Default/2023/11/361153340/RI/MR/XX/3098002/benq-eh620-projector-500x500.jpg",
        "alt": "BenQ EH620 Projector",
        "category": "Top Rated",
        "brand": "BenQ",
        "type":"projector",
        "numberofReviews": 22,
        "canWishlist": "false",
        "averageRating": 4.5,
        "productName": "BenQ EH620 Projector",
        "productLink": "BenQ-EH620-Projector",
        "price": "1,21,000",
        "description": "Innovative projector with exceptional clarity and brightness."
    },
    {
        "id": 6,
        "img": "https://5.imimg.com/data5/SELLER/Default/2023/11/361168694/GL/CT/RX/3098002/benq-ex600-projector-500x500.jpg",
        "alt": "BenQ EX600 Projector",
        "category": "Top Rated",
        "brand": "BenQ",
        "type":"projector",
        "numberofReviews": 12,
        "canWishlist": "false",
        "averageRating": 4.5,
        "productName": "BenQ EX600 Projector",
        "productLink": "BenQ-EX600-Projector",
        "price": "56,599",
        "description": "Compact and efficient projector, ideal for office and educational use."
    },
    {
        "id": 7,
        "img": "https://5.imimg.com/data5/SELLER/Default/2023/11/361169334/QG/KC/RO/3098002/benq-ms560p-projector-500x500.jpg",
        "alt": "BenQ MS560P Projector",
        "category": "Top Rated",
        "brand": "BenQ",
        "type":"projector",
        "numberofReviews": 4,
        "canWishlist": "false",
        "averageRating": 4.5,
        "productName": "BenQ MS560P Projector",
        "productLink": "BenQ-MS560P-Projector",
        "price": "32,500",
        "description": "Description of BenQ MS560P Projector"
    },
    {
        "id": 8,
        "img": "https://5.imimg.com/data5/SELLER/Default/2023/11/361149907/AF/CS/PO/3098002/benq-ms550-projector-500x500.jpg",
        "alt": "BenQ MS550 Meeting Room Projector",
        "category": "Top Rated",
        "brand": "BenQ",
        "type":"projector",
        "numberofReviews": 79,
        "canWishlist": "false",
        "averageRating": 4.5,
        "productName": "BenQ MS550 Meeting Room Projector",
        "productLink": "BenQ-MS550-Meeting-Room-Projector",
        "price": "31,500",
        "description": "Description of BenQ MS550 Meeting Room Projector"
    },
    {
        "id": 9,
        "img": "https://5.imimg.com/data5/SELLER/Default/2023/11/361166848/JU/WX/KL/3098002/benq-mx808pst-projector-500x500.jpg",
        "alt": "BenQ MX808PST+ Projector",
        "category": "Top Rated",
        "brand": "BenQ",
        "type":"projector",
        "numberofReviews": 63,
        "canWishlist": "false",
        "averageRating": 4.5,
        "productName": "BenQ MX808PST+ Projector",
        "productLink": "BenQ-MX808PST-Plus-Projector",
        "price": "50,000",
        "description": "Description of BenQ MX808PST+ Projector"
    },
    {
        "id": 10,
        "img": "https://5.imimg.com/data5/SELLER/Default/2023/11/361000660/QR/HV/IQ/3098002/xerox-photocopiers-500x500.jpg",
        "alt": "BenQ MX808STH Interactive Projector",
        "category": "Top Rated",
        "brand": "BenQ",
        "type":"projector",
        "numberofReviews": 38,
        "canWishlist": "false",
        "averageRating": 4.5,
        "productName": "BenQ MX808STH Interactive Projector",
        "productLink": "BenQ-MX808STH-Interactive-Projector",
        "price": "51,500",
        "description": "Description of BenQ MX808STH Interactive Projector"
    },
    {
        "id": 11,
        "img": "https://5.imimg.com/data5/SELLER/Default/2023/11/360999536/TT/DJ/HI/3098002/office-automation-service-500x500.jpg",
        "alt": "BenQ GS50 Potrable Projector",
        "category": "Top Rated",
        "brand": "BenQ",
        "type":"projector",
        "numberofReviews": 84,
        "canWishlist": "false",
        "averageRating": 4.5,
        "productName": "BenQ GS50 Potrable Projector",
        "productLink": "BenQ-GS50-Potrable-Projector",
        "price": "69,990",
        "description": "Description of BenQ GS50 Potrable Projector"
    },
    {
        "id": 12,
        "img": "https://5.imimg.com/data5/SELLER/Default/2023/11/361155103/FE/ZJ/LU/3098002/benq-th690st-projector-500x500.jpg",
        "alt": "BenQ Th690st Projector",
        "category": "Top Rated",
        "brand": "BenQ",
        "type":"projector",
        "numberofReviews": 99,
        "canWishlist": "false",
        "averageRating": 4.5,
        "productName": "BenQ Th690st Projector",
        "productLink": "BenQ-Th690st-Projector",
        "price": "1,09,990",
        "description": "Description of BenQ Th690st Projector"
    },
    {
        "id": 13,
        "img": "https://5.imimg.com/data5/SELLER/Default/2023/11/361155734/GD/MG/BT/3098002/benq-lw500st-projector-500x500.png",
        "alt": "BenQ LW500ST Projector",
        "category": "Top Rated",
        "brand": "BenQ",
        "type":"projector",
        "numberofReviews": 29,
        "canWishlist": "false",
        "averageRating": 4.5,
        "productName": "BenQ LW500ST Projector",
        "productLink": "BenQ-LW500ST-Projector",
        "price": "54,990",
        "description": "Description of BenQ LW500ST Projector"
    },
    {
        "id": 14,
        "img": "https://5.imimg.com/data5/SELLER/Default/2023/11/361155968/BX/ZQ/JQ/3098002/benq-mx550-projector-500x500.jpg",
        "alt": "BenQ MX550 Projector",
        "category": "Top Rated",
        "brand": "BenQ",
        "type":"projector",
        "numberofReviews": 76,
        "canWishlist": "false",
        "averageRating": 4.5,
        "productName": "BenQ MX550 Projector",
        "productLink": "BenQ-MX550-Projector",
        "price": "37,300",
        "description": "Description of BenQ MX550 Projector"
    },
    {
        "id": 15,
        "img": "https://5.imimg.com/data5/SELLER/Default/2023/11/360399256/RV/OF/VK/3098002/viewsonic-ls751hd-projector-500x500.jpg",
        "alt": "ViewSonic LS751HD Projector",
        "category": "Top Rated",
        "brand": "ViewSonic",
        "type":"projector",
        "numberofReviews": 98,
        "canWishlist": "false",
        "averageRating": 4.5,
        "productName": "ViewSonic LS751HD Projector",
        "productLink": "ViewSonic-LS751HD-Projector",
        "price": "2,80,000",
        "description": "Description of ViewSonic LS751HD Projector"
    },
    {
        "id": 16,
        "img": "https://5.imimg.com/data5/SELLER/Default/2023/11/361135043/PQ/TQ/XD/3098002/viewsonic-ls550whe-projector-500x500.jpg",
        "alt": "ViewSonic LS550WHE Projector",
        "category": "Top Rated",
        "brand": "ViewSonic",
        "type":"projector",
        "numberofReviews": 43,
        "canWishlist": "false",
        "averageRating": 4.5,
        "productName": "ViewSonic LS550WHE Projector",
        "productLink": "ViewSonic-LS550WHE-Projector",
        "price": "61,500",
        "description": "Description of ViewSonic LS550WHE Projector"
    },
    {
        "id": 17,
        "img": "https://5.imimg.com/data5/SELLER/Default/2023/11/361134787/UB/QO/DR/3098002/viewsonic-cpb701hdh-projector-500x500.jpg",
        "alt": "ViewSonic CPB701HD Projector",
        "category": "Top Rated",
        "brand": "ViewSonic",
        "type":"projector",
        "numberofReviews": 77,
        "canWishlist": "false",
        "averageRating": 4.5,
        "productName": "ViewSonic CPB701HD Projector",
        "productLink": "ViewSonic-CPB701HD-Projector",
        "price": "62,299",
        "description": "Description of ViewSonic CPB701HD Projector"
    },
    {
        "id": 18,
        "img": "https://5.imimg.com/data5/SELLER/Default/2023/11/360398543/CB/JA/KP/3098002/viewsonic-cpb701-4k-home-projector-500x500.jpg",
        "alt": "ViewSonic CPB701-4K Home Projector",
        "category": "Top Rated",
        "brand": "ViewSonic",
        "type":"projector",
        "numberofReviews": 1,
        "canWishlist": "false",
        "averageRating": 4.5,
        "productName": "ViewSonic CPB701-4K Home Projector",
        "productLink": "benq",
        "price": "1,18,900",
        "description": "Description of ViewSonic CPB701-4K Home Projector"
    },
    {
        "id": 19,
        "img": "https://5.imimg.com/data5/SELLER/Default/2023/11/360397098/JB/GH/QN/3098002/viewsonic-m1-g2-854x480-resolution-led-projecto-500x500.jpg",
        "alt": "ViewSonic M1+_G2 Smart  Portable Projector",
        "category": "Top Rated",
        "brand": "ViewSonic",
        "type":"projector",
        "numberofReviews": 69,
        "canWishlist": "false",
        "averageRating": 4.5,
        "productName": "ViewSonic M1+_G2 Smart  Portable Projector",
        "productLink": "benq",
        "price": "46,000",
        "description": "Description of ViewSonic M1+_G2 Smart  Portable Projector"
    },
    {
        "id": 20,
        "img": "https://5.imimg.com/data5/SELLER/Default/2023/11/360396412/PQ/GD/FC/3098002/viewsonic-pa503x-projector-500x500.jpg",
        "alt": "ViewSonic PA503X Projector",
        "category": "Top Rated",
        "brand": "ViewSonic",
        "type":"projector",
        "numberofReviews": 56,
        "canWishlist": "false",
        "averageRating": 4.5,
        "productName": "ViewSonic PA503X Projector",
        "productLink": "benq",
        "price": "39,700",
        "description": "Description of ViewSonic PA503X Projector"
    },
    {
        "id": 21,
        "img": "https://5.imimg.com/data5/SELLER/Default/2023/11/360395316/OG/GV/CK/3098002/viewsonic-pa503s-3-projector-500x500.jpg",
        "alt": "ViewSonic PA503S-3 Projector",
        "category": "Top Rated",
        "brand": "ViewSonic",
        "type":"projector",
        "numberofReviews": 55,
        "canWishlist": "false",
        "averageRating": 4.5,
        "productName": "ViewSonic PA503S-3 Projector",
        "productLink": "benq",
        "price": "29,990",
        "description": "Description of ViewSonic PA503S-3 Projector"
    },
    {
        "id": 22,
        "img": "https://5.imimg.com/data5/SELLER/Default/2023/11/361134778/LR/AA/SS/3098002/egate-i9-pro-max-android-projector-500x500.jpg",
        "alt": "EGATE I9 Pro Max Android Projector",
        "category": "Top Rated",
        "brand": "EGATE",
        "type":"projector",
        "numberofReviews": 76,
        "canWishlist": "false",
        "averageRating": 4.5,
        "productName": "EGATE I9 Pro Max Android Projector",
        "productLink": "benq",
        "price": "12,990",
        "description": "Description of EGATE I9 Pro Max Android Projector"
    },
    {
        "id": 23,
        "img": "https://5.imimg.com/data5/SELLER/Default/2023/11/361073635/EB/RF/QY/3098002/egate-k9-pro-max-android-projector-500x500.jpg",
        "alt": "EGATE K9 Pro Max Android Projector",
        "category": "Top Rated",
        "brand": "EGATE",
        "type":"projector",
        "numberofReviews": 37,
        "canWishlist": "false",
        "averageRating": 4.5,
        "productName": "EGATE K9 Pro Max Android Projector",
        "productLink": "benq",
        "price": "15,500",
        "description": "Description of EGATE K9 Pro Max Android Projector"
    },
    {
        "id": 24,
        "img": "https://5.imimg.com/data5/SELLER/Default/2023/11/361134831/VI/KS/AW/3098002/egate-l9-pro-android-projector-500x500.jpg",
        "alt": "EGATE L9 Pro Android Projector",
        "category": "Top Rated",
        "brand": "EGATE",
        "type":"projector",
        "numberofReviews": 76,
        "canWishlist": "false",
        "averageRating": 4.5,
        "productName": "EGATE L9 Pro Android Projector",
        "productLink": "benq",
        "price": "21,990",
        "description": "Description of EGATE L9 Pro Android Projector"
    },
    {
        "id": 25,
        "img": "https://5.imimg.com/data5/SELLER/Default/2023/11/360985723/WE/SX/AM/3098002/epson-digital-projector-500x500.jpg",
        "alt": "EGATE O9 Pro Zen Projector",
        "category": "Top Rated",
        "brand": "EGATE",
        "type":"projector",
        "numberofReviews": 14,
        "canWishlist": "false",
        "averageRating": 4.5,
        "productName": "EGATE O9 Pro Zen Projector",
        "productLink": "benq",
        "price": "25,990",
        "description": "Description of EGATE O9 Pro Zen Projector"
    },
    {
        "id": 26,
        "img": "https://5.imimg.com/data5/SELLER/Default/2023/11/361134818/AQ/KW/TS/3098002/egate-o9-pro-automatic-smart-projector-500x500.jpg",
        "alt": "EGATE O9 Pro Automatic Smart Projector",
        "category": "Top Rated",
        "brand": "EGATE",
        "type":"projector",
        "numberofReviews": 59,
        "canWishlist": "false",
        "averageRating": 4.5,
        "productName": "EGATE O9 Pro Automatic Smart Projector",
        "productLink": "benq",
        "price": "25,990",
        "description": "Description of EGATE O9 Pro Automatic Smart Projector"
    },
    {
        "id": 27,
        "img": "https://5.imimg.com/data5/SELLER/Default/2023/11/360394543/UM/LI/SZ/3098002/epson-eb-e01-xga-3lcd-projector-500x500.jpg",
        "alt": "Epson EB-E01 XGA 3LCD Projector",
        "category": "Top Rated",
        "brand": "Epson",
        "type":"projector",
        "numberofReviews": 5,
        "canWishlist": "false",
        "averageRating": 4.5,
        "productName": "Epson EB-E01 XGA 3LCD Projector",
        "productLink": "benq",
        "price": "33,333",
        "description": "Description of Epson EB-E01 XGA 3LCD Projector"
    },
    {
        "id": 28,
        "img": "https://5.imimg.com/data5/SELLER/Default/2023/11/361134899/HL/LB/BU/3098002/epson-co-fh02-lumen-projector-500x500.jpg",
        "alt": "Epson CO-FH02 Lumen Projector",
        "category": "Top Rated",
        "brand": "Epson",
        "type":"projector",
        "numberofReviews": 88,
        "canWishlist": "false",
        "averageRating": 4.5,
        "productName": "Epson CO-FH02 Lumen Projector",
        "productLink": "benq",
        "price": "80,000",
        "description": "Description of Epson CO-FH02 Lumen Projector"
    },
    {
        "id": 28,
        "img": "https://5.imimg.com/data5/SELLER/Default/2023/11/361134899/HL/LB/BU/3098002/epson-co-fh02-lumen-projector-500x500.jpg",
        "alt": "Hullo CO-FH02 Lumen Projector",
        "category": "Top Rated",
        "brand": "Epson",
        "type":"projector",
        "numberofReviews": 2,
        "canWishlist": "false",
        "averageRating": 3.5,
        "productName": "Hullo CO-FH02 Lumen Projector",
        "productLink": "benq",
        "price": "80,000",
        "description": "Description of Epson CO-FH02 Lumen Projector"
    }
]
# Transforming the data
transformed_projectors = []
for item in all_projectors:
    priceInt = item["price"].replace("₹ ", "").replace(",", "")
    transformed_projectors.append({
        "id": int(item["id"]),
        
        "price": item["price"].replace("₹ ", ""),
        "priceInt": int(priceInt),
        
    })

print(transformed_projectors)

