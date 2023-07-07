"use strict";
const BASEURL = `${window.location.protocol}//${window.location.host}`; //"http://127.0.0.1:8000";
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

    tanggal_transaksi.blur();
  });
}

////////////////////////////
// POPUP FOR SELECT MEMBER
///////////////////////////
const buttonMember = document.getElementById("pilih-anggota");
const viewMember = document.getElementById("modal-member");

const modalMember = new bootstrap.Modal(viewMember);

const tableMember = document.getElementById("table-member");
const member = document.getElementById("viewanggota");
const memberid = document.getElementById("anggota");
document.addEventListener("DOMContentLoaded", function () {
  let selectMembers = document.querySelectorAll("#select-member");

  selectMembers.forEach((button, index) => {
    button.addEventListener("click", () => {
      let id = document.querySelector(`#idmember${index + 1}`).textContent;
      let name = document.querySelector(`#namemember${index + 1}`).textContent;
      member.value = name;
      memberid.value = id;
      modalMember.hide();
      console.log(id, name, memberid);
      console.log(BASEURL);
    });
  });
});

if (buttonMember) {
  buttonMember.addEventListener("click", () => {
    modalMember.show();
  });
}

/////////////////////
//////flatpicker
flatpickr("input[type=datetime-local]", {
  enableTime: true,
  dateFormat: "Y-m-d H:i",
});

/////////////////////
//////dselect

 const id_anggota = document.getElementById("id_anggota");
 dselect(id_anggota, {
   search: true,
 });
