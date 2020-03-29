const initialState = {
  stores: [],
  location: {},
  radius: 1500,
  error: null,
  // for viewing
  current: null,
  marker: null,
  result: null
};

export default function reducer(state = initialState, action) {
  switch (action.type) {
    case 'SEARCH_LOCATION_PENDING': {
      return {
        ...state
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
        ...state
      };
    }
    case 'SEARCH_STORES_SUCCESS': {
      return {
        ...state,
        stores: action.payload.stores
      };
    }
    case 'SEARCH_SET_ERROR': {
      return {
        ...state,
        error: action.payload.error
      };
    }
    case 'HOVER_MARKER': {
      return {
        ...state,
        marker: action.payload.key
      };
    }
    case 'HOVER_RESULT': {
      return {
        ...state,
        result: action.payload.key
      };
    }
    case 'VIEW_DETAILED_INFO': {
      return {
        ...state,
        current: action.payload.key
      };
    }
    default:
      return state;
  }
}
