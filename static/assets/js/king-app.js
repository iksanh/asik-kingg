"use strict";
const checkPermission = document.getElementsByName("permissions");
const buttonCheckPermission = document.getElementById("btnPermissionCheck");
const buttonUnCheckPermission = document.getElementById("btnPermissionUnCheck");

if (buttonCheckPermission) {
  buttonCheckPermission.addEventListener("click", function () {
    checkList(checkPermission, true);
  });
}

if (buttonUnCheckPermission) {
  buttonUnCheckPermission.addEventListener("click", function () {
    checkList(checkPermission, false);
  });
}

function checkList(tag, command) {
  for (let i = 0; i < tag.length; i++) {
    //         command === true ? tag[i].checked = true : tag[i].checked = false
    tag[i].checked = command;
  }
}

const tanggal_transaksi = document.querySelector("#id_tanggal_transaksi");

if (tanggal_transaksi) {
  tanggal_transaksi.addEventListener("change", (event) => {
    console.log(event.target.value);
    console.log("Coba");
    tanggal_transaksi.blur();
  });
}
