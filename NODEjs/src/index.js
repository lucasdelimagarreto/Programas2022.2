const express = require('express')
const cors = require('cors')
const { v4: uuidv4 } = require('uuid')
const { request, response } = require('express')

const app = express()

app.use(cors())
app.use(express.json())

const users = []
function checkExistUserAccount(request, response, next){
    const { username } = request.headers
    const user = users.find(user => user.username === username)

    if (!user) {
        return response.status(404).json({error: "User does not exist"})
    }
    request.user = user

    next()
}

app.post('/users', (request, response)=>{
    const { name, username } = request.body
    const checkIfUserExist = users.some(user => user.username === username)
    if (checkIfUserExist) {
        return response.status(400).json({ error: 'Username alreaaady exists.'})
    }

    const newUser = {
        id: uuidv4(),
        name,
        username,
        todos: []
    }

    users.push(newUser)

    return response.status('201').json(newUser)
})

app.get("/todos", checkExistUserAccount, (request, response) => {
    const user = request.user

    return response.status(201).json(user.todos)
})

app.post('/todos', checkExistUserAccount, (request, response) => {
    const user = request.user
    const { title, deadline } = request.body
    const newTodo = {
        id: uuidv4(),
        title,
        done: false,
        deadline: new Date(deadline),
        created_at: new Date()
    }

    user.todos.push(newTodo)

    return response.status(201).json(newTodo)
})

app.listen(3333)