class News:

    def __init__(self, tit, des, img):

        self.tit = tit
        self.des = des 
        self.img = img 

news1 = News(
    "iPhone 16 Pro Max",
    "The iPhone 16 Pro Max, released in September 2024, features a 6.9-inch Super Retina XDR display with a 120Hz adaptive refresh rate, a titanium design with Ceramic Shield front, and a triple-camera system including a 48MP Fusion camera.",
    "https://github.com/NR1000-coder/Images/blob/main/iPhone.png?raw=true"
)

news2 = News(
    "The Apple AirPods Pro 3",
    "The Apple AirPods (3rd generation) offer improved features like personalized spatial audio, sweat and water resistance (IPX4), and a longer battery life with up to 6 hours of listening time on a single charge, and 30 hours total with the case. They also have a new design and are compatible with various Apple devices. ",
    "https://github.com/NR1000-coder/Images/blob/main/apple%20watch.jpg?raw=true"
)

news3 = News(
    "The Apple Watch Ultra 3",
    "The Apple Watch Ultra 3, expected to launch in late 2025, is rumored to bring several exciting upgrades, including 5G connectivity, satellite texting, and potential blood pressure monitoring. It's also rumored to have a brighter, larger display with a slimmer profile. ",
    "https://github.com/NR1000-coder/Images/blob/main/airpods.jpg?raw=true"
)

news_list = [news1, news2, news3]