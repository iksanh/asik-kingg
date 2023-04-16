const checkPermission  = document.getElementsByName('permissions')
const buttonCheckPermission = document.getElementById('btnPermissionCheck')
const buttonUnCheckPermission = document.getElementById('btnPermissionUnCheck')

buttonCheckPermission.addEventListener('click', function(){
      checkList(checkPermission, true);
});

buttonUnCheckPermission.addEventListener('click', function(){
    checkList(checkPermission, false);
})

function checkList(tag, command){

    for(let i= 0 ; i<tag.length; i++ ) {
//         command === true ? tag[i].checked = true : tag[i].checked = false
          tag[i].checked = command
    }

}



