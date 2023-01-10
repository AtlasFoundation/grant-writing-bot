import { Machine } from 'xstate';

const userManagementMachine = Machine({
    id: 'userManagement',
    initial: 'loggedOut',
    states: {
        loggedOut: {
            on: {
                LOGIN: 'loggedIn'
            }
        },
        loggedIn: {
            on: {
                LOGOUT: 'loggedOut'
            }
        }
    }
});
