
const routes = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/Welcome.vue') },
      { path: 'crypto', component: () => import('pages/Crypto.vue') },
      { path: 'math', component: () => import('pages/Math.vue') },
      { path: 'recipes', component: () => import('pages/Recipes.vue') },
      { path: 'theater', component: () => import('pages/Theater.vue') },
      { path: 'links', component: () => import('pages/Links.vue') },
    ]
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: '*',
    component: () => import('pages/Error404.vue')
  }
]

export default routes
