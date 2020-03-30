const initialState = {
  stores: [],
  location: {},
  radius: 8000,
  error: null,
  // for viewing
  current: null,
  marker: null,
  result: null,
  currentPopularTime: null,
  currentPopularDay: null,
  loader: false,
  searchTerm: '',
  searchType: 'stores'
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
        ...state,
        loader: true
      };
    }
    case 'SEARCH_STORES_SUCCESS': {
      return {
        ...state,
        stores: action.payload.stores,
        loader: false,
        searchType: 'stores'
      };
    }
    case 'SEARCH_ITEM_PENDING': {
      return {
        ...state,
        loader: true
      };
    }
    case 'SEARCH_ITEM_SUCCESS': {
      return {
        ...state,
        stores: action.payload.stores,
        loader: false,
        searchType: 'item'
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
    case 'UPDATE_POPULAR_TIME': {
      return {
        ...state,
        currentPopularTime: action.payload.hour,
        currentPopularDay: action.payload.day
      };
    }
    case 'UPDATE_SEARCH_TERM': {
      return {
        ...state,
        searchTerm: action.payload.term
      };
    }
    default:
      return state;
  }
}
