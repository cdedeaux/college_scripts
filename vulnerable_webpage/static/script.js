//learned from https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch
fetch("http://127.0.0.1:5000/crazyunfindablebackdoor", {
  method: "GET",
  headers: {
    "Authorization": "Basic " + btoa("trueadmin:admin123")
  }
});