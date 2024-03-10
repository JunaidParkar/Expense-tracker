class scrollManager {
  constructor() {
    this.dom = Dkit.init();
  }

  addListener() {
    this.dom.revert();
    this.removeListener();
    let card_parent = Array.from(this.dom.class("card-parent").get());
    this.dom.revert();

    card_parent.forEach((parent) => {
      parent.addEventListener("wheel", (e) => {
        this.addScroller(e, parent);
      });
    });
  }

  removeListener() {
    this.dom.revert();
    const card_parent = Array.from(this.dom.class("card-parent").get());
    this.dom.revert();

    card_parent.forEach((parent) => {
      parent.removeEventListener("wheel", (e) => {
        this.addScroller(e, parent);
      });
    });
  }

  addScroller(e, parent) {
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
  }
}

class monthlyStatsManager {
  constructor(monthlyStat, scroller) {
    this.monthlyStat = monthlyStat;
    this.dom = Dkit.init();
    this.scroller = scroller
  }

  init() {
    let stats = {};
    this.monthlyStat.forEach((stat) => {
      if (!stats[stat[1]]) {
        stats[stat[1]] = [];
      }
      stats[stat[1]].push({
        id: stat[0],
        year: stat[1],
        month: stat[2],
        income: parseFloat(stat[3]),
        expense: parseFloat(stat[4]),
        balance: parseFloat(stat[3]) - parseFloat(stat[4]),
      });
    });
    let dt = [];
    for (let yearData in stats) {
      dt.push({ yearData: stats[yearData], year: yearData });
    }
    dt.sort((a, b) => {
      return parseInt(b.year) - parseInt(a.year);
    });
    dt.forEach((dat) => {
      this.prepare_elements(dat.year, dat.yearData);
    });
    this.scroller.addListener();
  }

  prepare_elements(year, data) {
    let div = dom.create("div").get();
    this.dom.revert();
    div.classList.add("mainParent");
    let p1 = this.dom.create("p").get();
    this.dom.revert();
    p1.textContent = year;
    let div1 = this.dom.create("div").get();
    this.dom.revert();
    div1.classList.add("scroll-h", "card-parent");
    data.sort(this.sortByMonth);
    data.forEach((months) => {
      this.dom.revert();
      let divc = this.dom.create("div").get();
      divc.classList.add("card");
      divc.dataset.id = months.id;
      divc.dataset.year = months.year;
      let h4 = this.dom.create("h4").get();
      this.dom.revert();
      h4.textContent = months.month;
      let divC1 = this.dom.create("div").get();
      divC1.classList.add("inc");
      divC1.innerHTML = `Income: <span>${months.income}</span>`;
      this.dom.revert();
      let divC2 = this.dom.create("div").get();
      divC2.classList.add("exp");
      divC2.innerHTML = `Expense: <span>${months.expense}</span>`;
      this.dom.revert();
      let divC3 = this.dom.create("div").get();
      divC3.classList.add("sav");
      divC3.innerHTML = `Saving: <span>${months.balance}</span>`;
      this.dom.revert();
      divc.appendChild(h4);
      divc.appendChild(divC1);
      divc.appendChild(divC2);
      divc.appendChild(divC3);
      div1.appendChild(divc);
    });
    div.appendChild(p1);
    div.appendChild(div1);
    this.dom.revert();
    let mains = this.dom.id("expenses-slider-parent").get();
    this.dom.revert();
    mains.appendChild(div);
  }

  sortByMonth = (a, b) => {
    const monthsOrder = [
      "January",
      "February",
      "March",
      "April",
      "May",
      "June",
      "July",
      "August",
      "September",
      "October",
      "November",
      "December",
    ];

    const monthA = a.month;
    const monthB = b.month;

    return monthsOrder.indexOf(monthA) - monthsOrder.indexOf(monthB);
  };
}
