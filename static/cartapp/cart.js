var updateBtns = document.getElementsByClassName('update-cart')

for(var i = 0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click',function(){
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('ProductId :',productId,'Action :',action)
    })
}


function updateUserOrder(productId,action){
    console.log('User is logged in, sending data...')

    var url = '/update_item/'
}