class scrollManager {
  constructor() {
    this.dom = Dkit.init();
  }

  addListener() {
    
    this.removeListener();
    let card_parent = Array.from(this.dom.class("card-parent").get());
    

    card_parent.forEach((parent) => {
      parent.addEventListener("wheel", (e) => {
        this.addScroller(e, parent);
      });
    });
  }

  removeListener() {
    
    const card_parent = Array.from(this.dom.class("card-parent").get());
    

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
  constructor() {
    this.monthlyStat = null;
    this.dom = Dkit.init();
    this.scroller = new scrollManager()
  }

  init(stat) {
    this.monthlyStat = stat
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
    
    div.classList.add("mainParent");
    let p1 = this.dom.create("p").get();
    
    p1.textContent = year;
    let div1 = this.dom.create("div").get();
    
    div1.classList.add("scroll-h", "card-parent");
    data.sort(this.sortByMonth);
    data.forEach((months) => {
      
      let divc = this.dom.create("div").get();
      divc.classList.add("card");
      let h4 = this.dom.create("h4").get();
      
      h4.textContent = months.month;
      let divC1 = this.dom.create("div").get();
      divC1.classList.add("inc");
      divC1.innerHTML = `Income: <span>${months.income}</span>`;
      
      let divC2 = this.dom.create("div").get();
      divC2.classList.add("exp");
      divC2.innerHTML = `Expense: <span>${months.expense}</span>`;
      
      let divC3 = this.dom.create("div").get();
      divC3.classList.add("sav");
      divC3.innerHTML = `Saving: <span>${months.balance}</span>`;
      
      divc.appendChild(h4);
      divc.appendChild(divC1);
      divc.appendChild(divC2);
      divc.appendChild(divC3);
      this.cardClickr(divc, months.month, months.year)
      div1.appendChild(divc);
    });
    div.appendChild(p1);
    div.appendChild(div1);
    let mains = this.dom.id("expenses-slider-parent").get();
    
    mains.appendChild(div);
  }

  cardClickr(div, month, year) {
        div.addEventListener("click", e => {
          window.location.href = `expense.html?year=${year}&month=${month}`;
        });
  };

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

class expenseManager {
  constructor() {}

  async addExpense(amount, category, description, type, date) {
    return await eel.addTransaction(amount, category, description, type, date)()
  }

  async getSpecificStats(date) {
    return await eel.getSpecificStats(date)()
  }

  async getMonthlyStats() {
    return await eel.getMonthlyStats()()
  }

  structureMonthlyStat(stats) {
    let s = new monthlyStatsManager()
    s.init(stats)
  }
}