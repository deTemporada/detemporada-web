import React, { Component } from 'react'
import gql from 'graphql-tag';
import { graphql } from 'react-apollo';

class RecipeList extends Component {
	render() {
		console.log(this.props.recipeListQuery)
		if (this.props.recipeListQuery && this.props.recipeListQuery.loading) {
			return <div>Loading</div>
		}

		if (this.props.recipeListQuery && this.props.recipeListQuery.error) {
			return <div>Error: {this.props.recipeListQuery.error.message}</div>
		}


		const allRecipes = this.props.recipeListQuery.allRecipes
		return (
			<ul>
    			{ allRecipes.map( rp => <li key={rp.id}>{rp.name}</li> ) }
   			</ul>
   		)
	}



 }

 const RECIPE_LIST_QUERY = gql`
  query RecipeListQuery {
    allRecipes {
      id
      name
    }
  }
`;

export default graphql(RECIPE_LIST_QUERY, { name: 'recipeListQuery'})(RecipeList);