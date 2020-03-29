import { call, put, takeEvery } from 'redux-saga/effects';
import { storesApi } from './API';

export function* onStores() {
  yield takeEvery('SEARCH_API_STORES', fetchStores);
}

export function* fetchStores(action) {
  try {
    yield put({ type: 'SEARCH_STORES_PENDING', payload: {} });

    const stores = yield call(storesApi, action.payload);
    // const stores = {
    //   data: {
    //     stores: [
    //       {
    //         address: '8792 Sacramento Drive # A, Alexandria',
    //         id: 'ce2bbb17a579d6abfa0c9f3be1f92b874a157d94',
    //         location: { lat: 38.7209265, lng: -77.1264499 },
    //         name: 'Super Mini Mart',
    //         place_id: 'ChIJTSne-Eest4kRRV-NRv15w_Y'
    //       }
    //     ]
    //   }
    // };

    yield put({
      type: 'SEARCH_STORES_SUCCESS',
      payload: { stores: stores.data.stores }
    });
  } catch (e) {
    yield put({ type: 'SEARCH_SET_ERROR', payload: { error: e.message } });
  }
}
