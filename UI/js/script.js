const dom = Dkit.init();

dom.revert();
dom.id("cursor");

const cc = new customCursor(dom.get(), false);
cc.getCursor();
dom.revert();

dom.id("expenses-slider-parent");
const slider_parent = dom.get();
dom.revert();

dom.class("card-parent");
const card_parent = Array.from(dom.get());
dom.revert();

card_parent.forEach((parent) => {
  parent.addEventListener("wheel", (e) => {
    if (
      (e.deltaY > 0 &&
        parent.scrollLeft + parent.clientWidth === parent.scrollWidth) ||
      (e.deltaY < 0 &&
        parent.scrollLeft + parent.clientWidth === parent.clientWidth)
    ) {
      return;
    } else {
      e.preventDefault();
      parent.scrollLeft += e.deltaY;
    }
  });
});

dom.id("expenses-slider-parent")
const expense_history_container = dom.get()
dom.revert()

const prepare_parents = () => {
    let div = dom.create("div").get()
    dom.revert()
    div.classList.add("mainParent")
    let p1 = dom.create("p").get()
    dom.revert()
    let div1 = dom.create("div").get()
    dom.revert()
    div1.classList.add("scroll-h", "card-parent")
    div.appendChild(p1)
    div.appendChild(div1)
    console.log(div)
}

prepare_parents()

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

for (const year in expenses) {
  console.log(year);
}
