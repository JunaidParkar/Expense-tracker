const dom = Dkit.init();
const scroller = new scrollManager()

scroller.addListener()

dom.revert();
dom.id("cursor");

const cc = new customCursor(dom.get(), false);
cc.getCursor();
dom.revert();

let expenses = {
  2020: {
    May: [
      (1, 55999.0, "2020-04-25", "gaming", "Brought Xbox", "2024-03-05"),
      (2, 55999.0, "2020-04-25", "gaming", "Brought Xbox", "2024-03-05"),
    ],
    April: [
      (1, 400.0, "2020-03-25", "gaming", "RFS subscription", "2024-03-05"),
      (2, 400.0, "2020-03-25", "gaming", "RFS subscription", "2024-03-05"),
    ],
  },
  2024: {
    April: [
      (1, 20000.0, "2024-03-25", "gaming", "Brought PS5", "2024-03-05"),
      (2,
      100000.0,
      "2024-03-30",
      "workplace",
      "Currency exchange INR to dihram",
      "2024-03-05"),
      (3, 20000.0, "2024-03-25", "gaming", "Brought PS5", "2024-03-05"),
      (4,
      100000.0,
      "2024-03-30",
      "workplace",
      "Currency exchange INR to dihram",
      "2024-03-05"),
    ],
    March: [
      (1,
      6000.0,
      "2024-02-25",
      "laptop acessories",
      "Purchased SSD",
      "2024-03-05"),
      (2,
      6000.0,
      "2024-02-25",
      "laptop acessories",
      "Purchased SSD",
      "2024-03-05"),
    ],
  },
};

const monthlyStat = [
  [1, 2024, "January", 201000.0, 12000.0, "2024-01-20"],
  [2, 2024, "February", 200000.0, 4000.0, "2024-02-20"],
  [2, 2024, "May", 200000.0, 4000.0, "2024-02-20"],
  [2, 2024, "November", 200000.0, 4000.0, "2024-02-20"],
  [2, 2024, "September", 200000.0, 4000.0, "2024-02-20"],
  [2, 2024, "October", 200000.0, 4000.0, "2024-02-20"],
  [2, 2024, "July", 200000.0, 4000.0, "2024-02-20"],
  [2, 2024, "March", 200000.0, 4000.0, "2024-02-20"],
  [3, 2023, "April", 200000.0, 4000.0, "2023-01-20"],
];

const monthlyStatManager = new monthlyStatsManager(monthlyStat, scroller)
monthlyStatManager.init()