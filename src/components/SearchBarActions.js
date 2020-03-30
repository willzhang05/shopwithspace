export function updateTerm(term) {
  return {
    type: 'UPDATE_SEARCH_TERM',
    payload: { term }
  };
}

export function searchStores() {
  return (dispatch, getState) => {
    const state = getState();

    const payload = {
      longitude: state.location.longitude,
      latitude: state.location.latitude,
      item: state.searchTerm,
      radius: state.radius
    };
    if (payload.item.length > 0) {
      dispatch(getStoresForItem(payload));
    } else {
      dispatch(getNearbyStores(payload));
    }
  };
}

function getStoresForItem(payload) {
  return {
    type: 'SEARCH_API_ITEM',
    payload: payload
  };
}

function getNearbyStores(payload) {
  return {
    type: 'SEARCH_API_STORES',
    payload: payload
  };
}
