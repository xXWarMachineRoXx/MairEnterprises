import { VendureConfig } from '@vendure/core';

export const config: VendureConfig = {
    // ...
    authOptions: {
        tokenMethod: ['bearer', 'cookie'],
    },
};