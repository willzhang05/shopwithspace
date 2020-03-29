import { call, put, takeEvery } from 'redux-saga/effects';
import { storesApi } from './API';

export function* onStores() {
  yield takeEvery('SEARCH_API_STORES', fetchStores);
}

export function* fetchStores(action) {
  try {
    yield put({ type: 'SEARCH_STORES_PENDING', payload: {} });

    // const stores = yield call(storesApi, action.payload);
    const stores = storesSample.data.stores.map((store, index) => {
      if (
        'current_popularity' in store.popular &&
        store.popular.current_popularity < 0
      ) {
        const currentTime = Date.now();
        const currentDay = (currentTime.getDay() + 6) % 7;
        const currentMins = currentTime.getMinutes();
        const currentHour = currentTime.getHours();

        const byHour = store.popular.populartimes[6].data;
        store.popular.current_popularity =
          ((60.0 - currentMins) / 60.0) * byHour[currentHour % 24] +
          (currentMins / 60.0) *
            store.popular.populartimes[(currentDay + 1) % 7].data[0];
      }
      return store;
    });
    yield put({
      type: 'SEARCH_STORES_SUCCESS',
      payload: { stores: stores }
    });
  } catch (e) {
    yield put({ type: 'SEARCH_SET_ERROR', payload: { error: e.message } });
  }
}

const storesSample = {
  data: {
    stores: [
      // {
      //   current_speed: 30.0,
      //   details: {
      //     formatted_address:
      //       '8792 Sacramento Dr # A, Alexandria, VA 22309, USA',
      //     formatted_phone_number: '(703) 799-2640',
      //     photo_ref:
      //       'CmRaAAAA9LN7OEMWDW57awrwmzpVLS4r_nigNr3JczuMuQ68spJkej0HQPxjZWF11H4cEHCpYYnggiaTdllSAF352j5a-dSNYJBgAWPCPV9wh_OtI_VVRcLD5u7IO3T9AcC3k9e3EhA1goCrESjSGqdJ51-XSwIAGhTCyloQoFsEHdKrZHf8QIWi7eyp-g'
      //   },
      //   free_flow_speed: 30.0,
      //   id: 'ce2bbb17a579d6abfa0c9f3be1f92b874a157d94',
      //   location: { lat: 38.7209265, lng: -77.1264499 },
      //   name: 'Super Mini Mart',
      //   photo:
      //     'https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight500&photoreference=CmRaAAAA9LN7OEMWDW57awrwmzpVLS4r_nigNr3JczuMuQ68spJkej0HQPxjZWF11H4cEHCpYYnggiaTdllSAF352j5a-dSNYJBgAWPCPV9wh_OtI_VVRcLD5u7IO3T9AcC3k9e3EhA1goCrESjSGqdJ51-XSwIAGhTCyloQoFsEHdKrZHf8QIWi7eyp-g&key=AIzaSyCl3oN8un11v0d7DGCJ9QQYEh7nf93Vu0Q',
      //   place_id: 'ChIJTSne-Eest4kRRV-NRv15w_Y',
      //   popular: {},
      //   safety: 1.0
      // },
      {
        current_speed: 26.0,
        details: {
          formatted_address: '8723 Cooper Rd D, Alexandria, VA 22309, USA',
          formatted_phone_number: '(703) 799-8886',
          website: 'www.google.com',
          icon: 'https://www.google.com/s2/favicons?domain=www.walmart.com',
          photo_ref:
            'CmRaAAAADBmo1PSaRpIgW1SDA5ukWtI5DF1lhgDAI45BuhQ9ucBq9TS3ilFuYLzfTKxVTYk9gWpGXsAiYWuNCTjjeH6P7YXP0-qnz2glUxlG81l5PEGF7ja8Cwld4XKWZONmbAxxEhAG7HWN8XPj-hunllFrtzRDGhROOaDgR6qBw_0WbnhGiZsOgsQotA'
        },
        free_flow_speed: 32.0,
        id: '8cbaf37e7f2468013bc2cfe365cb9cc2d804a00f',
        location: { lat: 38.7202608, lng: -77.1241144 },
        name: 'AMIGOS DELI & SUPERMARKET',
        photo:
          'https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight500&photoreference=CmRaAAAADBmo1PSaRpIgW1SDA5ukWtI5DF1lhgDAI45BuhQ9ucBq9TS3ilFuYLzfTKxVTYk9gWpGXsAiYWuNCTjjeH6P7YXP0-qnz2glUxlG81l5PEGF7ja8Cwld4XKWZONmbAxxEhAG7HWN8XPj-hunllFrtzRDGhROOaDgR6qBw_0WbnhGiZsOgsQotA&key=AIzaSyCl3oN8un11v0d7DGCJ9QQYEh7nf93Vu0Q',
        place_id: 'ChIJizz_1xKtt4kRDlHkZc0O_vs',
        popular: {
          current_popularity: 0.8,
          populartimes: [
            {
              data: [
                0,
                0,
                0,
                0,
                0,
                0,
                2,
                17,
                37,
                51,
                45,
                28,
                8,
                2,
                8,
                22,
                37,
                40,
                28,
                11,
                2,
                0,
                0,
                0
              ],
              name: 'Monday'
            },
            {
              data: [
                0,
                0,
                0,
                0,
                0,
                0,
                8,
                31,
                31,
                25,
                37,
                40,
                31,
                17,
                11,
                17,
                25,
                31,
                25,
                14,
                2,
                0,
                0,
                0
              ],
              name: 'Tuesday'
            },
            {
              data: [
                0,
                0,
                0,
                0,
                0,
                0,
                2,
                14,
                28,
                40,
                42,
                37,
                25,
                17,
                14,
                17,
                22,
                22,
                17,
                8,
                2,
                0,
                0,
                0
              ],
              name: 'Wednesday'
            },
            {
              data: [
                0,
                0,
                0,
                0,
                0,
                0,
                8,
                20,
                28,
                34,
                34,
                25,
                14,
                11,
                17,
                25,
                34,
                37,
                31,
                20,
                8,
                0,
                0,
                0
              ],
              name: 'Thursday'
            },
            {
              data: [
                0,
                0,
                0,
                0,
                0,
                0,
                2,
                62,
                51,
                5,
                37,
                51,
                17,
                2,
                2,
                14,
                28,
                34,
                28,
                14,
                2,
                0,
                0,
                0
              ],
              name: 'Friday'
            },
            {
              data: [
                0,
                0,
                0,
                0,
                0,
                0,
                2,
                25,
                65,
                85,
                71,
                42,
                34,
                34,
                37,
                37,
                34,
                25,
                17,
                8,
                2,
                0,
                0,
                0
              ],
              name: 'Saturday'
            },
            {
              data: [
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                22,
                74,
                100,
                68,
                31,
                25,
                28,
                25,
                20,
                22,
                17,
                2,
                0,
                0,
                0,
                0
              ],
              name: 'Sunday'
            }
          ],
          time_spent: 15,
          time_wait: 15
        },
        safety: 4.25
      }
      // {
      //   current_speed: 37.0,
      //   details: {
      //     formatted_address: '8736 Richmond Hwy, Alexandria, VA 22309, USA',
      //     formatted_phone_number: '(703) 780-1241',
      //     photo_ref:
      //       'CmRaAAAAryFVwjgdI6baSkTfdQm_tYaZfegbJxIHgNs2B1TcFR6mkn0dtA_F02okv33BMsbxfdou9TadUVw2Dammvh9VP-b7XyFJ6AZaquQWVAsMazp37Wl2ttKvddB0ueBqSeWqEhB-o6IRzpjZJ8mGVou0l-6bGhRH8nHP1W3Dhn3A5mEJm9m3Xi1iiQ'
      //   },
      //   free_flow_speed: 37.0,
      //   id: 'cf1c65d9431423a0aebdbae92ea79b77d7935212',
      //   location: { lat: 38.7222976, lng: -77.1247155 },
      //   name: 'La Vaquita Supermarket',
      //   photo:
      //     'https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight500&photoreference=CmRaAAAAryFVwjgdI6baSkTfdQm_tYaZfegbJxIHgNs2B1TcFR6mkn0dtA_F02okv33BMsbxfdou9TadUVw2Dammvh9VP-b7XyFJ6AZaquQWVAsMazp37Wl2ttKvddB0ueBqSeWqEhB-o6IRzpjZJ8mGVou0l-6bGhRH8nHP1W3Dhn3A5mEJm9m3Xi1iiQ&key=AIzaSyCl3oN8un11v0d7DGCJ9QQYEh7nf93Vu0Q',
      //   place_id: 'ChIJ80RDwzest4kRP1eBVLwSSS4',
      //   popular: {},
      //   safety: 5.0
      // }
    ]
  }
};
