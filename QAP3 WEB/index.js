// Desc: A program to create invoices for Mo's Lawncare Services.
// Author:Lucas 
// Dates: 07/12/2025 - 07/??/2025


//TODO:
// 1. Add error messages for invalid inputs.
// 2. Format Phone Number.


var $ = function (id) {
  return document.getElementById(id);
};


// Define format options for printing.
const cur2Format = new Intl.NumberFormat("en-CA", {
  style: "currency",
  currency: "CAD",
  minimumFractionDigits: "2",
  maximumFractionDigits: "2",
});

const per2Format = new Intl.NumberFormat("en-CA", {
  style: "percent",
  minimumFractionDigits: "2",
  maximumFractionDigits: "2",
});

const com2Format = new Intl.NumberFormat("en-CA", {
  style: "decimal",
  minimumFractionDigits: "2",
  maximumFractionDigits: "2",
});


// Define program constants.
const TAX_RATE = 0.15;
const ENV_TAX_RATE = 0.014;

// Start main program here.
let FirstName = prompt("Enter the customer's first name:");
let LastName = prompt("Enter the customer's last name:");
let StAddress = prompt("Enter the customer's street address:");
let City = prompt("Enter the customer's city:");
let Phone = prompt("Enter the customer's phone number (999-999-9999):");

let PropSQFT = prompt("Enter the property's square footage:");
PropSQFT = parseFloat(PropSQFT);

let CustName = FirstName + " " + LastName;

// Perform program calculations.
let Border = PropSQFT * 0.04;
let BorderCost = Border * 0.35;

let LawnSQFT = PropSQFT - Border;
let LawnCost = LawnSQFT * 0.07;
let FertilizerCost = PropSQFT * 0.05;

let Subtotal = BorderCost + LawnCost + FertilizerCost;
let Tax = Subtotal * TAX_RATE;
let EnvTax = Subtotal * ENV_TAX_RATE;
let Total = Subtotal + Tax + EnvTax;

// Display the invoice.
document.writeln("<br />");
document.writeln("<table class='InvoiceTable'>");

document.writeln("<tr class='BoldOrangeCenter'><td colspan='2'>Mo's Lawncare Services - Customer Invoice</td></tr>");

document.writeln("<tr><td colspan='2'><br />Customer Details: <br /><br /><span class='centertext'>" + CustName + "<br /> " + StAddress + "<br /> " + City + " " + Phone + "</span><br /> <br /> Property Size (in sq feet): " + PropSQFT + "<br /><br /></td></tr>");

document.writeln("<tr><td>Border Cost:</td><td class='RightText'>" + cur2Format.format(BorderCost) + "</td></tr>");
document.writeln("<tr><td>Moving Cost:</td><td class='RightText'>" + cur2Format.format(LawnCost) + "</td></tr>");
document.writeln("<tr><td>Fertilizer Cost:</td><td class='RightText'>" + cur2Format.format(FertilizerCost) + "</td></tr>");
document.writeln("<tr><td> <br /> </td><td> <br /> </td></tr>");
document.writeln("<tr><td>Sales Tax (HST):</td><td class='RightText'>" + cur2Format.format(Tax) + "</td></tr>");
document.writeln("<tr><td>Environmental Tax:</td><td class='RightText'>" + cur2Format.format(EnvTax) + "</td></tr>");
document.writeln("<tr><td> <br /> </td><td> <br /> </td></tr>");
document.writeln("<tr><td>Invoice Total:</td><td class='RightText'>" + cur2Format.format(Total) + "</td></tr>");
document.writeln("<tr class='BoldOrangeCenter'><td colspan='2'>Turning Lawns into Landscapes</td></tr>");

document.writeln("</table>");