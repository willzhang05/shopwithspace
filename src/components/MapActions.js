export function getStores() {
  return (dispatch, getState) => {
    const state = getState();

    const payload = {
      longitude: state.location.longitude,
      latitude: state.location.latitude,
      radius: state.radius
    };
    dispatch(getNearbyStores(payload));
  };
}

function getNearbyStores(payload) {
  return {
    type: 'SEARCH_API_STORES',
    payload: payload
  };
}
