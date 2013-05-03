function [theta, J_history] = gradientDescent(X, y, theta, alpha, num_iters)
%GRADIENTDESCENT Performs gradient descent to learn theta
%   theta = GRADIENTDESENT(X, y, theta, alpha, num_iters) updates theta by 
%   taking num_iters gradient steps with learning rate alpha

% Initialize some useful values
m = length(y); % number of training examples
J_history = zeros(num_iters, 1);

for iter = 1:num_iters

    % ====================== YOUR CODE HERE ======================
    % Instructions: Perform a single gradient step on the parameter vector
    %               theta. 
    %
    % Hint: While debugging, it can be useful to print out the values
    %       of the cost function (computeCost) and gradient here.
    %

	%	http://stackoverflow.com/questions/10479353/gradient-descent-seems-to-fail
	tmp_j1 = 0;
	for i = 1:m
		tmp_j1 = tmp_j1 + ((theta(1,1) + theta(2,1) * X(i,2)) - y(i));
	end
	tmp_j2 = 0;
	for i = 1:m
		tmp_j2 = tmp_j2 + ((theta(1,1) + theta(2,1) * X(i,2)) - y(i)) * X(i,2);
	end
	tmp1 = theta(1,1) - (alpha * ((1/m) * tmp_j1))
	tmp2 = theta(2,1) - (alpha * ((1/m) * tmp_j2))

	theta(1,1) = tmp1
	theta(2,1) = tmp2





    % ============================================================

    % Save the cost J in every iteration    
    J_history(iter) = computeCost(X, y, theta);

end

end
