const data = [
  {
    category: "상의",
    brand: "Supreme",
    product: "슈프림 박스로고 후드티",
    price: "390,000",
  },
  {
    category: "하의",
    brand: "DIESEL",
    product: "디젤 트랙 팬츠",
    price: "188,000",
  },
  {
    category: "신발",
    brand: "Nike",
    product: "에어포스 1",
    price: "137,000",
  },
  {
    category: "패션잡화",
    brand: "Music&Goods",
    product: "빵빵이 키링",
    price: "29,000",
  },
];

const dataTable = document.getElementById("data-table");

data.forEach((item) => {
  const row = dataTable.insertRow();
  row.insertCell(0).innerHTML = item.category;
  row.insertCell(1).innerHTML = item.brand;
  row.insertCell(2).innerHTML = item.product;
  row.insertCell(3).innerHTML = item.price;
});
