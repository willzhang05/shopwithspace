const initialState = {
  stores: [],
  loader: false,
  location: {},
  radius: 1500,
  error: null
};

export default function reducer(state = initialState, action) {
  switch (action.type) {
    case 'SEARCH_LOCATION_PENDING': {
      return {
        ...state,
        loader: true
      };
    }
    case 'SEARCH_LOCATION_SUCCESS': {
      return {
        ...state,
        location: action.payload.location
      };
    }
    case 'SEARCH_STORES_PENDING': {
      return {
        ...state,
        loader: true
      };
    }
    case 'SEARCH_STORES_SUCCESS': {
      return {
        ...state,
        loader: false,
        stores: action.payload.stores
      };
    }
    case 'SEARCH_SET_ERROR': {
      return {
        ...state,
        error: action.payload.error
      };
    }
    default:
      return state;
  }
}
