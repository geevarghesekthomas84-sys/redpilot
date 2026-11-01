fetch("http://worldtimeapi.org/api/timezone/Etc/UTC")
  .then(response => response.json())
  .then(data => console.log(data.datetime));
