//SEARCH FUNCTION FOR USERS TABLE
function searchUsers() {
  
    let rowCountO = 0;
    let inputO, filterO, tableO, trO, i;
    let tdO0, tdO1, tdO2, tdO3;
    let txtValO0, txtValO1, txtValO2, txtValO3;
    inputO = $('#searchUsers').val();
    console.log(inputO)
    filterO = inputO.toUpperCase();
    tableO = document.getElementById("myTable");
    trO = tableO.getElementsByTagName("tr");
    for (i = 0; i < trO.length; i++) {
      tdO0 = trO[i].getElementsByTagName("td")[0];
      tdO1 = trO[i].getElementsByTagName("td")[1];
      tdO2 = trO[i].getElementsByTagName("td")[2];
      tdO3 = trO[i].getElementsByTagName("td")[3];
  
      if (tdO1 || tdO2 || tdO3 ) {
        txtValO0 = tdO0.textContent || tdO0.innerText;
        txtValO1 = tdO1.textContent || tdO1.innerText;
        txtValO2 = tdO2.textContent || tdO2.innerText;
        txtValO3 = tdO3.textContent || tdO3.innerText;
        if (txtValO0.toUpperCase().indexOf(filterO) > -1 || txtValO1.toUpperCase().indexOf(filterO) > -1 || txtValO2.toUpperCase().indexOf(filterO) > -1 || txtValO3.toUpperCase().indexOf(filterO) > -1 ) {
          trO[i].style.display = "";
          rowCountO++;
        } else {
          trO[i].style.display = "none";
        }
      };       
    };
    if (rowCountO == 0) {
      $("#no-search").css("display", "block");
    } else {
      $("#no-search").css("display", "none");
      rowCountO = 0;
    }
  };



//SEARCH FUNCTION FOR EMPLOYEE TABLE
function searchEmployee() {
  
    let rowCountO = 0;
    let inputO, filterO, tableO, trO, i;
    let tdO0, tdO1, tdO2;
    let txtValO0, txtValO1, txtValO2;
    inputO = $('#searchEmployee').val();
    console.log(inputO)
    filterO = inputO.toUpperCase();
    tableO = document.getElementById("myTableE");
    trO = tableO.getElementsByTagName("tr");
    for (i = 0; i < trO.length; i++) {
      tdO0 = trO[i].getElementsByTagName("td")[0];
      tdO1 = trO[i].getElementsByTagName("td")[1];
      tdO2 = trO[i].getElementsByTagName("td")[2];
  
      if (tdO1 || tdO2 ) {
        txtValO0 = tdO0.textContent || tdO0.innerText;
        txtValO1 = tdO1.textContent || tdO1.innerText;
        txtValO2 = tdO2.textContent || tdO2.innerText;
        if (txtValO0.toUpperCase().indexOf(filterO) > -1 || txtValO1.toUpperCase().indexOf(filterO) > -1 || txtValO2.toUpperCase().indexOf(filterO) > -1) {
          trO[i].style.display = "";
          rowCountO++;
        } else {
          trO[i].style.display = "none";
        }
      };       
    };
    if (rowCountO == 0) {
      $("#no-searchE").css("display", "block");
    } else {
      $("#no-searchE").css("display", "none");
      rowCountO = 0;
    }
};



//SEARCH FUNCTION FOR ATTENDANCE TABLE
function searchAttendance() {
  
    let rowCountO = 0;
    let inputO, filterO, tableO, trO, i;
    let tdO0, tdO1, tdO2;
    let txtValO0, txtValO1, txtValO2;
    inputO = $('#searchAttendance').val();
    console.log(inputO)
    filterO = inputO.toUpperCase();
    tableO = document.getElementById("myTableA");
    trO = tableO.getElementsByTagName("tr");
    for (i = 0; i < trO.length; i++) {
      tdO0 = trO[i].getElementsByTagName("td")[0];
      tdO1 = trO[i].getElementsByTagName("td")[1];
      tdO2 = trO[i].getElementsByTagName("td")[2];
  
      if (tdO1 || tdO2 ) {
        txtValO0 = tdO0.textContent || tdO0.innerText;
        txtValO1 = tdO1.textContent || tdO1.innerText;
        txtValO2 = tdO2.textContent || tdO2.innerText;
        if (txtValO0.toUpperCase().indexOf(filterO) > -1 || txtValO1.toUpperCase().indexOf(filterO) > -1 || txtValO2.toUpperCase().indexOf(filterO) > -1) {
          trO[i].style.display = "";
          rowCountO++;
        } else {
          trO[i].style.display = "none";
        }
      };       
    };
    if (rowCountO == 0) {
      $("#no-searchA").css("display", "block");
    } else {
      $("#no-searchA").css("display", "none");
      rowCountO = 0;
    }
};



//SEARCH FUNCTION FOR PAYROLL TABLE
function searchPayroll() {
  
    let rowCountO = 0;
    let inputO, filterO, tableO, trO, i;
    let tdO0, tdO1;
    let txtValO0, txtValO1;
    inputO = $('#searchPayroll').val();
    console.log(inputO)
    filterO = inputO.toUpperCase();
    tableO = document.getElementById("myTableP");
    trO = tableO.getElementsByTagName("tr");
    for (i = 0; i < trO.length; i++) {
      tdO0 = trO[i].getElementsByTagName("td")[0];
      tdO1 = trO[i].getElementsByTagName("td")[1];
      if (tdO1) {
        txtValO0 = tdO0.textContent || tdO0.innerText;
        txtValO1 = tdO1.textContent || tdO1.innerText;
        if (txtValO0.toUpperCase().indexOf(filterO) > -1 || txtValO1.toUpperCase().indexOf(filterO) > -1) {
          trO[i].style.display = "";
          rowCountO++;
        } else {
          trO[i].style.display = "none";
        }
      };       
    };
    if (rowCountO == 0) {
      $("#no-searchP").css("display", "block");
    } else {
      $("#no-searchP").css("display", "none");
      rowCountO = 0;
    }
};