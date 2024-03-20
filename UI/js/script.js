const scroller = new scrollManager();
const expenseM = new expenseManager()
scroller.addListener();

const head = dom.tag("head").get()[0];

const renderSpecificMonthData = async (date) => {
  let datas = await expenseM.getSpecificStats(date)
  let expense = 0
  let income = 0
  datas.forEach(data => {
    let tr = dom.create("tr").get()
    tr.dataset.id = data[0]
    let td1 = dom.create("td").get()
    let td2 = dom.create("td").get()
    let td3 = dom.create("td").get()
    let td4 = dom.create("td").get()
    let td5 = dom.create("td").get()
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
    expense = data[6] == "negative" ? expense + data[1] : expense
    income = data[6] == "negative" ? income : income + data[1]
    dom.id("table").get().appendChild(tr)
  });
  dom.id("recieved").get().textContent = income.toFixed(2)
  dom.id("spend").get().textContent = expense.toFixed(2)
  dom.id("saving").get().textContent = (income - expense).toFixed(2)
}

if (dom.from(head).tag("title").get()[0].textContent == "Expense") {
  var params = new URLSearchParams(window.location.search);
  var year = params.get("year");
  var month = params.get("month");
  if (!year || !month) {
    window.location.href = "index.html";
  }
  dom.id("heading").get().textContent = month + " " + year;
  let months = [
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
  renderSpecificMonthData(`${year}-${months.indexOf(month) + 1}`);
}

const getBack = () => (window.location.href = "index.html");

const manageMonthlyStat = async () => {
  let stat = await expenseM.getMonthlyStats()
  if (stat) {
    expenseM.structureMonthlyStat(stat)
  }
};

if (dom.id("expenses-slider-parent").get()) {
  manageMonthlyStat()
}

const expenseForm = dom.id("expenseForm").get();

const addTransaction = () => {
  let amount = dom.id("amount").get().value
  let type = dom.id("type").get().value;
  let description = dom.id("description").get().value
  let date = dom.id("date").get().value
  let category = dom.id("category").get().value
  let confElem = Array.from(dom.class("confirm_screen").get())[0]
  confElem.style.display = "flex"
  dom.from(confElem).id("heading_conf").get().textContent = "Are you sure you want to continue with these data?"
  let html = `<div><h5>Amount: <span>${amount}</span></h5><h5>Description: <span>${description}</span></h5><h5>Type: <span>${type}</span></h5><h5>Category: <span>${category}</span></h5><h5>Date: <span>${date}</span></h5></div><div class="action_buttons_confirm"><div onclick="addExpenseToDB('${amount}', '${category}', '${description}', '${type == "Check In" ? "positive" : "negative"}', '${date}')"><p>Continue</p></div><div onclick="cancel_conf()"><p>Cancel</p></div></div>`;
  dom.from(confElem).id("body_conf").get().innerHTML += html
};


if (expenseForm) {
  let formV = new FormValidator(
    expenseForm,
    true,
    [],
    [
      {
        type: "custom_required",
        func: showMessage,
      },
    ]
  );
  formV.validate(() => {
    addTransaction()
  });
}

const addExpenseToDB = async (amount, category, description, type, date) => {
  await expenseM.addExpense(amount, category, description, type, date)
  window.location.reload()
}