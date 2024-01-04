#!/usr/bin/node
const request = require('request');
const apiURL = process.argv[2];

request.get(apiURL, (error, response, body) => {
  if (error) {
    console.error('Error:', error.message);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Error:', `Received status code ${response.statusCode}`);
    return;
  }

  try {
    const tasksData = JSON.parse(body);

    const completedTasks = tasksData.filter(task => task.completed);

    const userCompletedTasks = completedTasks.reduce((acc, task) => {
      const userId = task.userId;
      acc[userId] = (acc[userId] || 0) + 1;
      return acc;
    }, {});

    console.log(JSON.stringify(userCompletedTasks, null, 2).replace(/"/g, "'"));
  } catch (parseError) {
    console.error('Error parsing JSON:', parseError.message);
  }
});
