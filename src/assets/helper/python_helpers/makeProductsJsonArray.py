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

# Transforming the data
transformed_projectors = []
for item in all_projectors:
    transformed_projectors.append({
        "id": int(item["id"]),
        "img": item["img"]["src"],
        "alt": item["img"]["alt"],
        "category": "Top Rated",
        "numberofReviews": random.randint(1, 100),  # Random number for demo
        "productName": item["name"],
        "price": item["price"].replace("₹ ", ""),
        "description": f"Description of {item['name']}"  # Placeholder description
    })

print(transformed_projectors)

