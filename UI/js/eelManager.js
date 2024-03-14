let stats = [
  [1, 2022, "January", 2393.52, 481.08, "2022-01"],
  [3, 2022, "February", 0.0, 498.6, "2022-02"],
  [4, 2022, "February", 611.92, 0.0, "2022-02"],
  [5, 2022, "March", 0.0, 430.33, "2022-03"],
  [6, 2022, "March", 3095.22, 0.0, "2022-03"],
  [7, 2022, "April", 0.0, 489.28, "2022-04"],
  [8, 2022, "April", 1271.52, 0.0, "2022-04"],
  [9, 2022, "May", 0.0, 439.71, "2022-05"],
  [10, 2022, "May", 2100.98, 0.0, "2022-05"],
  [11, 2022, "June", 0.0, 364.09, "2022-06"],
  [12, 2022, "June", 440.9, 0.0, "2022-06"],
  [13, 2022, "July", 0.0, 251.71, "2022-07"],
  [14, 2022, "July", 4969.52, 0.0, "2022-07"],
  [15, 2022, "August", 0.0, 528.05, "2022-08"],
  [16, 2022, "August", 1443.58, 0.0, "2022-08"],
  [17, 2022, "September", 0.0, 355.76, "2022-09"],
  [18, 2022, "September", 858.36, 0.0, "2022-09"],
  [19, 2022, "October", 0.0, 371.65, "2022-10"],
  [20, 2022, "October", 3811.58, 0.0, "2022-10"],
  [21, 2022, "November", 0.0, 447.89, "2022-11"],
  [22, 2022, "November", 2359.64, 0.0, "2022-11"],
  [23, 2022, "December", 0.0, 387.44, "2022-12"],
  [24, 2022, "December", 3147.5, 0.0, "2022-12"],
  [25, 2023, "January", 0.0, 436.99, "2023-01"],
  [26, 2023, "January", 1109.25, 0.0, "2023-01"],
  [27, 2023, "February", 0.0, 183.68, "2023-02"],
  [28, 2023, "February", 2587.0, 0.0, "2023-02"],
  [29, 2023, "March", 0.0, 260.09, "2023-03"],
  [30, 2023, "March", 333.7, 0.0, "2023-03"],
  [31, 2023, "April", 0.0, 295.8, "2023-04"],
  [32, 2023, "April", 4988.13, 0.0, "2023-04"],
  [33, 2023, "May", 0.0, 384.06, "2023-05"],
  [34, 2023, "May", 2129.27, 0.0, "2023-05"],
  [35, 2023, "June", 0.0, 330.51, "2023-06"],
  [36, 2023, "June", 3195.34, 0.0, "2023-06"],
  [37, 2023, "July", 0.0, 513.28, "2023-07"],
  [38, 2023, "July", 2301.51, 0.0, "2023-07"],
  [39, 2023, "August", 0.0, 462.68, "2023-08"],
  [40, 2023, "August", 2063.42, 0.0, "2023-08"],
  [41, 2023, "September", 0.0, 222.94, "2023-09"],
  [42, 2023, "September", 4742.72, 0.0, "2023-09"],
  [43, 2023, "October", 0.0, 337.9, "2023-10"],
  [44, 2023, "October", 3895.76, 0.0, "2023-10"],
  [45, 2023, "November", 0.0, 288.95, "2023-11"],
  [46, 2023, "November", 2117.55, 0.0, "2023-11"],
  [47, 2023, "December", 0.0, 463.37, "2023-12"],
  [48, 2023, "December", 3734.96, 0.0, "2023-12"],
  [49, 2024, "January", 0.0, 231.1, "2024-01"],
  [50, 2024, "January", 936.73, 0.0, "2024-01"],
  [51, 2024, "February", 0.0, 397.49, "2024-02"],
  [52, 2024, "February", 2139.81, 0.0, "2024-02"],
  [53, 2024, "March", 0.0, 241.78, "2024-03"],
  [54, 2024, "March", 576.68, 0.0, "2024-03"],
  [55, 2024, "April", 0.0, 321.36, "2024-04"],
  [56, 2024, "April", 541.52, 0.0, "2024-04"],
  [57, 2024, "May", 0.0, 355.91, "2024-05"],
  [58, 2024, "May", 2689.84, 0.0, "2024-05"],
  [59, 2024, "June", 0.0, 361.45, "2024-06"],
  [60, 2024, "June", 3238.06, 0.0, "2024-06"],
  [61, 2024, "July", 0.0, 304.75, "2024-07"],
  [62, 2024, "July", 2512.45, 0.0, "2024-07"],
  [63, 2024, "August", 0.0, 246.2, "2024-08"],
  [64, 2024, "August", 3066.58, 0.0, "2024-08"],
  [65, 2024, "September", 0.0, 275.51, "2024-09"],
  [66, 2024, "September", 951.22, 0.0, "2024-09"],
  [67, 2024, "October", 0.0, 300.12, "2024-10"],
  [68, 2024, "October", 4501.64, 0.0, "2024-10"],
  [69, 2024, "November", 0.0, 376.22, "2024-11"],
  [70, 2024, "November", 3526.54, 0.0, "2024-11"],
  [71, 2024, "December", 0.0, 387.64, "2024-12"],
  [72, 2024, "December", 1403.24, 0.0, "2024-12"],
];

const manageMonthlyStat = async () => {
  // let stat = await eel.getMonthlyStats()();
  let stat = stats;
  let scroller = new scrollManager();
  const monthlyStatManager = new monthlyStatsManager(stat, scroller);
  monthlyStatManager.init();
  cardClickr()
};

dom.revert();
if (dom.id("expenses-slider-parent").get()) {
  manageMonthlyStat()
}

let monthStat = [
  [1,
  33590.00,
  "2024-01",
  "Rent",
  "Salary",
  "2024-03-11",
  "positive"],
  [2,
  45.12,
  "2024-01",
  "Utilities",
  "Electricity bill",
  "2024-03-11",
  "negative"],
  [3,
  86.86,
  "2024-01",
  "Groceries",
  "Monthly grocery shopping",
  "2024-03-11",
  "negative"],
];

const showSpecificMonthData = async (date) => {
  let datas = await eel.getSpecificStats(date)()
  console.log(datas)
  // let datas = monthStat
  let expense = 0
  let income = 0
  datas.forEach(data => {
    dom.revert()
    let tr = dom.create("tr").get()
    dom.revert()
    tr.dataset.id = data[0]
    let td1 = dom.create("td").get()
    dom.revert()
    let td2 = dom.create("td").get()
    dom.revert()
    let td3 = dom.create("td").get()
    dom.revert()
    let td4 = dom.create("td").get()
    dom.revert()
    let td5 = dom.create("td").get()
    dom.revert()
    td1.textContent = data[2]
    td2.textContent = data[1]
    td3.textContent = data[3]
    td4.textContent = data[4]
    td5.textContent = data[6] == "negative" ? "Check out" : "Check in"
    tr.appendChild(td1)
    tr.appendChild(td2)
    tr.appendChild(td3)
    tr.appendChild(td4)
    tr.appendChild(td5)
    dom.revert()
    expense = data[6] == "negative" ? expense + data[1] : expense
    income = data[6] == "negative" ? income : income + data[1]
    dom.id("table").get().appendChild(tr)
    dom.revert()
  });
  dom.revert()
  dom.id("recieved").get().textContent = income.toFixed(2)
  dom.revert()
  dom.id("spend").get().textContent = expense.toFixed(2)
  dom.revert()
  dom.id("saving").get().textContent = (income - expense).toFixed(2)
  dom.revert()
}