#!/usr/bin/node
const request = require('request');
const apiUrl = process.argv[2];

request.get(apiUrl, (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
    const todos = JSON.parse(body);
    const completedTasks = todos.filter((todo) => todo.completed === true);
    const completedTasksByUserId = {};
    completedTasks.forEach((todo) => {
      if (!completedTasksByUserId[todo.userId]) {
        completedTasksByUserId[todo.userId] = 0;
      }
      completedTasksByUserId[todo.userId]++;
    });
    console.log(completedTasksByUserId);
  }
});
