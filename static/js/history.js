// Sample transaction data (you would fetch this data from a server in a real app)
const transactions = [
    { date: "2023-09-30", description: "Payment from User A",transactionId:"TW2049940", amount: 100.00 },
    { date: "2023-09-29", description: "Purchase at Online Store",transactionId:"TW2049940", amount: -50.00 },
    // Add more transactions here
];

const transactionTable = document.getElementById("transactionTable");
const tbody = transactionTable.querySelector("tbody");

// Function to populate the table with transaction data
function populateTable() {
    tbody.innerHTML = '';
    transactions.forEach(transaction => {
        const row = document.createElement("tr");
        row.innerHTML = `
            <td>${transaction.date}</td>
            <td>${transaction.description}</td>
            <td>${transaction.transactionId}</td>
            <td>${transaction.amount.toFixed(2)}</td>
        `;
        tbody.appendChild(row);
    });
}

// Call the function to populate the table when the page loads
window.onload = populateTable;
