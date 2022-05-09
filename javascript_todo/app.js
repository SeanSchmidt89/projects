
const ul = document.querySelector('#ul')
const button = document.querySelector('#button')
let inputTodo = document.querySelector('#inputName')
let inputDescription = document.querySelector('#inputDescription')


button.addEventListener('click', function(e){
    e.preventDefault()
    let newLi = document.createElement('li')
    newLi.innerText = `${inputTodo.value}`

    let deleteBtn = document.createElement('button')
    deleteBtn.innerText = 'Delete'
    deleteBtn.addEventListener('click', function(e){
        ul.removeChild(newLi)
    })
    
    let completeBtn = document.createElement('button')
    completeBtn.innerText = 'Complete'
    completeBtn.addEventListener('click', function(e){
        newLi.style.textDecoration = 'line-through'
    })

    
    newLi.append(completeBtn)
    newLi.append(deleteBtn)
    let descriptionUl = document.createElement('ul')
    let descriptionLi = document.createElement('li')
    descriptionLi.innerText = `${inputDescription.value}`
    
    newLi.append(descriptionUl)
    descriptionUl.appendChild(descriptionLi)
    
    
    ul.append(newLi)
    
    inputTodo.value = ''
    inputDescription.value = ''
})