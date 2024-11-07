
    function addTask() {
        const todoInput = document.getElementById('todoInput');
        const taskText = todoInput.value;

        if(taskText === '')
            return; //Previne a adição de tarefas vazias
        
        const todoList = document.getElementById('todoList');
        //Criando um novo item da lista
        const listItem = document.createElement('li');
        listItem.textContent = taskText;

        //botão de deletar
        const deleteBtn = document.createElement('span');
        deleteBtn.textContent = 'X';
        deleteBtn.className = 'delete-btn';
        deleteBtn.onclick = function(){
            todoList.removeChild(listItem);
        };
        //Adiciona o botão ao item da lista e o item a lista

        listItem.appendChild(deleteBtn);
        todoList.appendChild(listItem);

        //Limpa o campo de entrada
        todoInput.value = '';
    }

