export function initializeApp() {
  return dispatch => {
    dispatch(getLocation());
  };
}

export function getLocation() {
  return {
    type: 'SEARCH_API_LOCATION',
    payload: {}
  };
}
