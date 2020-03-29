import axios from 'axios';

var getPosition = function(options) {
  return new Promise(function(resolve, reject) {
    navigator.geolocation.getCurrentPosition(resolve, reject, options);
  });
};

export async function locationApi() {
  const data = await getPosition();
  const location = {
    longitude: data.coords.longitude,
    latitude: data.coords.latitude
  };
  return location;
}

export async function storesApi(payload) {
  console.log(payload);
  const stores = await axios.get('/nearby', {
    params: payload
  });
  return stores;
}
